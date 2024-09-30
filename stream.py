import streamlit as st  # Importing the Streamlit library for creating web applications
import pandas as pd  # Importing Pandas for data manipulation and analysis
import matplotlib.pyplot as plt  # Importing Matplotlib for plotting graphs
import seaborn as sns  # Importing Seaborn for making statistical graphics
import time  # Importing the time module for adding delays (e.g., simulating processing time)


# Include custom font using HTML and CSS
 # Using Streamlit's markdown function to write HTML and CSS
st.markdown("""
    <link rel="preconnect" href="https://fonts.googleapis.com">  # Preconnecting to Google's font service for faster loading
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>  # Preconnecting to the font CDN for cross-origin access
    <link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@300;400;500;600;700&display=swap" rel="stylesheet"> # Linking to the Fredoka font styles from Google Fonts
    <style>
        body {
            font-family: 'Fredoka', sans-serif; # Setting the font family for the body to Fredoka
        }
        h1 {
            color: #1DB954;  # Setting the color of h1 headers to Spotify green
        }
        p {
            color: #FFFFFF;  # Setting the color of paragraphs to white
        }
    </style>
""", unsafe_allow_html=True)  # Allowing the use of HTML in Streamlit

# Display header and instructions
st.markdown("<h1>Spotify Music Data Explorer</h1>", unsafe_allow_html=True) # Displaying a main header for the app
st.markdown("<p>Use this app to explore and visualize the Spotify dataset.</p>", unsafe_allow_html=True)




# Load your dataset
 # Caching the data loading function to optimize performance; it will only reload the data if the input changes
@st.cache_data
def load_data(): 
    file_path = "K:\STreamlit\dataset.csv"  
    data = pd.read_csv(file_path)
    return data
st.video("K:\STreamlit\introVid.mp4") 
# Display header and instructions
st.title("Spotify Music Data Explorer")
st.write("Use this app to explore and visualize the Spotify dataset.")
with st.spinner("Loading your data..."):# Displaying a spinner while the data is loading to indicate processing
    data = load_data()
    time.sleep(3)  # Simulate loading delay


# Sidebar filters
st.sidebar.header("Filters")
# Creating a sidebar header for filters, where users can select options to filter the data
# Filter by Popularity
# Creating a slider in the sidebar to allow users to select a range for popularity (0 to 100)
# The default range is set from 0 to 100
popularity_range = st.sidebar.slider("Select Popularity Range:", 0, 100, (0, 100))
# Filter by Genre
genres = data['track_genre'].unique()# Extracting the unique genres from the 'track_genre' column in the dataset
selected_genres = st.sidebar.multiselect("Select Genres:", genres, default=genres)
# Creating a multiselect box in the sidebar, allowing users to select one or more genres to filter by
# The default selection includes all genres
# Apply filters to data
filtered_data = data[
    (data['popularity'] >= popularity_range[0]) &  # Filtering data where popularity is greater than or equal to the minimum range
    (data['popularity'] <= popularity_range[1]) &  # Filtering data where popularity is less than or equal to the maximum range
    (data['track_genre'].isin(selected_genres))# Filtering data to include only the selected genres
]

# Display filtered data
st.subheader(f"Filtered Spotify Tracks ({len(filtered_data)} results)")# The f-string is used to insert the length of the 'filtered_data' (number of rows) into the text
# This informs the user how many tracks meet the filter criteria they selected
st.write(filtered_data)
# Data visualization
st.subheader("Data Visualizations")


# Select a limited number of rows for plotting
# Selecting the first 100 rows of the filtered data to limit the dataset for plotting
df_limited = filtered_data.iloc[:100]
# Create the line plot
plt.plot(df_limited.index, df_limited['danceability'], label='Danceability', color='green')
# Plotting the 'danceability' values for the limited dataset with green color and labeling the line as 'Danceability'
plt.plot(df_limited.index, df_limited['energy'], label='Energy', color='red')
plt.title('Line Plot of Danceability and Energy')
plt.xlabel('Track Index')
plt.ylabel('Values')
plt.legend()
# Display the plot in Streamlit
st.pyplot(plt)
# Rendering the plot inside the Streamlit app using st.pyplot




# Popularity Distribution
st.write("### Popularity Distribution")
fig, ax = plt.subplots()
sns.histplot(filtered_data['popularity'], bins=20, ax=ax)# Using Seaborn to create a histogram of the 'popularity' column from the filtered data
# 'bins=20' sets the number of bins (groups) for the distribution
st.pyplot(fig)

# Genre Distribution
st.write("### Genre Distribution")#3rd degree
fig2, ax2 = plt.subplots(figsize=(40, 24))# Creating a figure and axis using Matplotlib to hold the plot
genre_counts = filtered_data['track_genre'].value_counts()# Counting the occurrences of each genre in the filtered data
sns.barplot(x=genre_counts.index, y=genre_counts.values, ax=ax2)
# Using Seaborn to create a bar plot
# x=genre_counts.index specifies the genres, and y=genre_counts.values specifies the corresponding counts
plt.xticks(rotation=60)
plt.xticks(fontsize=36)
st.pyplot(fig2)

# Popularity vs. Danceability Scatter Plot
st.write("### Popularity vs Danceability")
fig3, ax3 = plt.subplots()
sns.scatterplot(x='popularity', y='danceability', data=filtered_data, ax=ax3)
st.pyplot(fig3)


# Top 10 Most Frequent Artists
st.write("### Top 10 Most Frequent Artists")
popular_artists = filtered_data['artists'].value_counts().head(10)
st.write(popular_artists) 
fig4, ax4 = plt.subplots()
sns.barplot(x=popular_artists.values, y=popular_artists.index, ax=ax4)
# Using Seaborn to create a horizontal bar plot, with the number of tracks on the x-axis and the artist names on the y-axis
plt.xlabel('Number of Tracks')
plt.title('Top 10 Most Frequent Artists')
st.pyplot(fig4)

# Top 10 Most Frequent Tracks
st.write("### Top 10 Most Frequent Tracks")
popular_tracks = filtered_data['track_name'].value_counts().head(10)
st.write(popular_tracks)
fig, ax = plt.subplots()
sns.barplot(x=popular_tracks.values, y=popular_tracks.index, ax=ax)
plt.xlabel('Number of Occurrences')
plt.title('Top 10 Most Frequent Tracks')
st.pyplot(fig)


# Footer
st.write("made by ")
st.write("#####    Janson V Johnson")
