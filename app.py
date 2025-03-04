import streamlit as st
import time
from datetime import datetime

# Page configuration for title and icon
st.set_page_config(page_title="Digital Clock", page_icon="⏰")

# CSS styles for colorful text
st.markdown("""
    <style>
    .title1 {
        color: #1E90FF;  /* Bright yellow for title */
        font-size: 36px;
        font-weight: bold;
        text-align: center;
    }
    .title2 {
        color: #fc03fc;
        font-size: 36px;
        font-weight: bold;
        text-align: center;
    }
    .author {
        color: #fc03fc !important;  /* Light purple for author name */
        font-size: 20px;
        text-align: center;
        font-weight: bold;
        margin-top: 20px;
    }
    .clock {
        text-align: center;
        font-weight: bold;
        font-size: 60px;
        padding: 20px;
    }
    .hours {
        color: #FF4500;  /* Bright orange-red for hours */
    }
    .minutes {
        color: #32CD32;  /* Bright lime green for minutes */
    }
    .seconds {
        color: #1E90FF;  /* Bright dodger blue for seconds */
    }
    </style>
""", unsafe_allow_html=True)

# Display title at the top
st.markdown("<div class='title1'>🐍 Learn Python 🐍</div>", unsafe_allow_html=True)
st.markdown("<div class='title2'>🕒 Digital Clock 🕒</div>", unsafe_allow_html=True)

# Create a placeholder for the clock
clock_placeholder = st.empty()

# Function to display the clock
def show_clock():
    while True:
        # Get current time
        now = datetime.now()
        hours = now.strftime("%H")
        minutes = now.strftime("%M")
        seconds = now.strftime("%S")
        
        # Create HTML for colorful time display
        time_html = f"""
        <div class='clock'>
            <span class='hours'>{hours}</span>:
            <span class='minutes'>{minutes}</span>:
            <span class='seconds'>{seconds}</span>
        </div>
        """
        
        # Display the time dynamically
        clock_placeholder.markdown(time_html, unsafe_allow_html=True)
        time.sleep(1)

        # Display author name at the bottom
st.markdown("<div class='author'>Author: Azmat Ali</div>", unsafe_allow_html=True)

# Run the clock
show_clock()



