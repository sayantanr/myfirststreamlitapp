import streamlit as st
import pandas as pd
import numpy as np
import time

st.title("my app")
st.header("my love")

st.subheader("Python is currently the most widely used multi-purpose, high-level programming language.")
st.markdown("#####hi####")
st.info("this is an information")
st.warning("this is an warning")
st.success("succeessful")
st.help(range)
url = st.text_input('https://www.sublimetext.com/docs/linux_repositories.html')
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
'first column': [1, 2, 3, 4],
'second column': [10, 20, 30, 40]
}))
chart_data = pd.DataFrame(
np.random.randn(20, 3),
columns=['a', 'b', 'c'])
st.line_chart(chart_data)
map_data = pd.DataFrame(
np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
columns=['lat', 'lon'])
st.map(map_data)
st.write("""Python is currently the most widely used multi-purpose, high-level programming language.
Python allows programming in Object-Oriented and Procedural paradigms.
Python programs generally are smaller than other programming languages like Java. Programmers have to type relatively less and indentation requirement of the language, makes them readable all the time.
Python language is being used by almost all tech-giant companies like – Google, Amazon, Facebook, Instagram, Dropbox, Uber… etc.
The biggest strength of Python is huge collection of standard library which can be used for the following:

    Machine Learning
    GUI Applications (like Kivy, Tkinter, PyQt etc. )
    Web frameworks like Django (used by YouTube, Instagram, Dropbox)
    Image processing (like OpenCV, Pillow)
    Web scraping (like Scrapy, BeautifulSoup, Selenium)
    Test frameworks
    Multimedia
    Scientific computing
    Text processing and many more """)
st.video('https://www.youtube.com/watch?v=DIHn5TN-7uM')
st.error("this is an error,Danger")
# Forms can be declared using the 'with' syntax
with st.form(key='form'):
    text_input = st.text_input(label='Enter your name')
    submit_button = st.form_submit_button(label='Submit')
st.text('This will appear first')
# Appends some text to the app.
my_slot1 = st.empty()
# Appends an empty slot to the app. We'll use this later.
my_slot2 = st.empty()
# Appends another empty slot.
st.text('This will appear last')
# Appends some more text to the app.
my_slot1.text('This will appear second')
# Replaces the first empty slot with a text string.
my_slot2.line_chart(np.random.randn(20, 2))
# Replaces the second empty slot with a chart.
progress_bar = st.progress(0)
status_text = st.empty()
chart = st.line_chart(np.random.randn(10, 2))
for i in range(100):
# Update progress bar.
    progress_bar.progress(i + 1)
    new_rows = np.random.randn(10, 2)
    # Update status text.
    status_text.text(
    'The latest random number is: %s' % new_rows[-1, 1])
    # Append data to the chart.
    chart.add_rows(new_rows)
    # Pretend we're doing some computation that takes time.
    time.sleep(0.1)
    status_text.text('Done!')
    st.balloons()

# Get some data.
data = np.random.randn(10, 2)
# Show the data as a chart.
chart = st.line_chart(data)
# Wait 1 second, so the change is clearer.
time.sleep(1)
# Grab some more data.
data2 = np.random.randn(10, 2)
# Append the new data to the existing chart.
chart.add_rows(data2)
'''Draw a title and some text to the app:

# This is the document title
This is some _markdown_.
'''
df = pd.DataFrame({'col1': [1,2,3]})
df # <-- Draw the dataframe
x = 10
'x', x
# <-- Draw the string 'x' and then the value of x
from PIL import Image
img = Image.open("index.jpeg")
st.image(img,width=500,caption="computer programming")
vid_file=open("y.mp4","rb").read()
st.video(vid_file)


import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import scipy as sp
chart_data = pd.DataFrame(

np.random.randn(20, 3),

columns=['a', 'b', 'c'])

st.area_chart(chart_data)
df = pd.DataFrame(

np.random.randn(10, 5),

columns=('col %d' % i for i in range(5)))

st.table(df)
import streamlit as st
import plotly.figure_factory as ff
import numpy as np
# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2
# Group data together
hist_data = [x1, x2, x3]
group_labels = ['Group 1', 'Group 2', 'Group 3']
# Create distplot with custom bin_size
fig = ff.create_distplot(
hist_data, group_labels, bin_size=[.1, .25, .5])
# Plot!
st.plotly_chart(fig, use_container_width=True)
import streamlit as st
import plotly.figure_factory as ff
import numpy as np
# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2
# Group data together
hist_data = [x1, x2, x3]
group_labels = ['Group 1', 'Group 2', 'Group 3']
# Create distplot with custom bin_size
fig = ff.create_distplot(
hist_data, group_labels, bin_size=[.1, .25, .5])
# Plot!
st.plotly_chart(fig, use_container_width=600)
st.cache()
