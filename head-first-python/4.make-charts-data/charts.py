import swimclub

FN = "Darius-13-100m-Fly.txt"


def generate_chart(filename):
    (swimmer, age, distance, stroke, times, average) = swimclub.read_swim_data(filename)
    title = swimmer + " (Under " + age + ") " + distance + " " + stroke

    # Convert times to hundredths for bar width calculation
    converts = []
    for t in times:
        if ":" in t:
            minutes, rest = t.split(":")
            seconds, hundredths = rest.split(".")
        else:
            minutes = 0
            seconds, hundredths = t.split(".")
        converts.append(
            (int(minutes) * 60 * 100) + (int(seconds) * 100) + int(hundredths)
        )

    # Find max time for scaling
    max_time = max(converts)

    # Generate HTML
    html = f"""<!doctype html>
                <html>
                <head>
                    <title>{title}</title>
                </head>
                <body>
                    <h3>{title}</h3>
"""

    for i, (time_str, time_hundredths) in enumerate(zip(times, converts), 1):
        # Scale bar width (max 400px)
        bar_width = int((time_hundredths / max_time) * 400)
        html += f"""    <svg height="30" width="400">
      <rect height="30" width="{bar_width}" style="fill: rgb(0, 0, 255)" /></svg
    >{time_str}<br />
"""

    html += f"""    <p>Average time: {average}</p>
  </body>
</html>"""

    # Save to HTML file
    html_filename = filename.replace(".txt", ".html")
    with open(html_filename, "w") as f:
        f.write(html)

    return html_filename


print(generate_chart(FN))
