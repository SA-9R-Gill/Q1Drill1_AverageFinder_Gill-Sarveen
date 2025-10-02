from pyscript import document, window

def compute_average(event):
    try:
        # Values from input fields
        social = float(document.getElementById("social").value)
        math = float(document.getElementById("math").value)
        science = float(document.getElementById("science").value)
        english = float(document.getElementById("english").value)
        filipino = float(document.getElementById("filipino").value)

        # Compute average score
        average = (social + math + science + english + filipino) / 5

        # Determiner of pass/fail
        if average >= 75:
            result = "✅ Passed"
            popup_msg = f"Congratulations! 🎉\nYour average is {round(average, 2)}.\nYou Passed!"
        else:
            result = "❌ Failed"
            popup_msg = f"Sorry! 😢\nYour average is {round(average, 2)}.\nYou Failed."

        # It display results on page
        document.getElementById("average").innerText = str(round(average, 2))
        document.getElementById("result").innerText = result

        # Show popup
        window.alert(popup_msg)

    except ValueError:
        # Handle missing/invalid inputs
        document.getElementById("average").innerText = "Invalid input"
        document.getElementById("result").innerText = "Invalid input"
        window.alert("⚠️ Invalid input! Please enter valid scores for all subjects.")
