import openai
import tkinter as tk
from tkinter import messagebox

# Set up the ChatG PT API
openai.api_key = "YOUR_API_KEY_HERE"

# Create the GUI window
root = tk.Tk()
root.title("Personal AI App")

# Create a text input field
input_field = tk.Text(root, height=10, width=40)
input_field.pack()

# Create a button to send the message
def send_message():
    message = input_field.get("1.0", tk.END)
    # Send the message to the ChatGPT API and display the response
    messages = [
        {"role": "system", "content": "You are a friendly and helpful assistant. You are knowledgeable about technology and science."},
        {"role": "user", "content": message}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    chat_message = response['choices'][0]['message']['content']
    output_field.insert(tk.END, f"Bot: {chat_message}\n")

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

# Create a text area to display the conversation
output_field = tk.Text(root, height=10, width=40)
output_field.pack()

# Run the app
if __name__ == "__main__":
    root.mainloop()
