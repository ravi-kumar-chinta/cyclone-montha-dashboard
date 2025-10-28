import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Set page config to wide mode
st.set_page_config(
    page_title="Cyclone Montha Dashboard", 
    layout="wide",
    initial_sidebar_state="expanded" # Keep sidebar open by default
)

# --- v8 DATASET (17 Districts) ---
data = {
    'District': ['Kakinada', 'Konaseema', 'Eluru', 'Krishna', 'Visakhapatnam', 'Nellore', 
                 'Prakasam', 'Guntur', 'Bapatla', 'Anakapalli', 'Srikakulam', 'Vizianagaram',
                 'Tirupati', 'Parvathipuram Manyam', 'Alluri Sitharama Raju', 'East Godavari', 'West Godavari'],
    'lat': [16.9891, 16.5500, 16.7118, 16.1650, 17.6868, 14.4426, 15.7866, 16.3067, 15.8700, 17.6880, 18.2938, 18.1121,
            13.6288, 18.7733, 17.8740, 17.0000, 16.7800],
    'lon': [82.2473, 81.9000, 81.1025, 81.1663, 83.2185, 79.9865, 79.1384, 80.4365, 80.4500, 83.0030, 83.8988, 83.4116,
            79.4192, 83.4246, 82.5358, 81.7600, 81.1200],
    'Max_WindSpeed_kmph': [110, 105, 95, 90, 85, 75, 70, 80, 88, 82, 65, 70,
                           60, 55, 70, 100, 92],
    'Total_Rainfall_mm': [280, 310, 220, 210, 180, 150, 130, 160, 190, 175, 110, 120,
                          140, 100, 230, 290, 215],
    'Evacuated_People': [45000, 52000, 22000, 18000, 15000, 9000, 6000, 12000, 14000, 11000, 5000, 4000,
                         8000, 3000, 16000, 48000, 20000],
    'Shelters_Setup': [60, 55, 30, 25, 20, 18, 10, 15, 22, 16, 8, 7,
                       12, 5, 20, 58, 28],
    'Power_Resumed_%': [30, 25, 50, 60, 65, 80, 85, 75, 70, 68, 90, 88,
                        82, 95, 40, 28, 52],
    'Alert_Level': ['Red', 'Red', 'Red', 'Orange', 'Orange', 'Yellow', 'Yellow', 'Orange', 'Red', 'Orange', 'Yellow', 'Yellow',
                    'Yellow', 'Yellow', 'Orange', 'Red', 'Red'],
    'Food_Packets': [50000, 60000, 25000, 20000, 18000, 10000, 7000, 15000, 16000, 12000, 6000, 5000,
                     9000, 4000, 18000, 55000, 22000],
    'Medical_Teams': [15, 18, 8, 7, 6, 4, 3, 5, 6, 5, 2, 2,
                      4, 2, 7, 16, 9],
    'Water_Litres': [100000, 120000, 50000, 45000, 40000, 25000, 20000, 30000, 35000, 28000, 15000, 12000,
                     22000, 10000, 40000, 110000, 48000],
    'Comms_Resumed_%': [20, 15, 40, 55, 60, 70, 75, 65, 60, 62, 85, 80,
                        75, 90, 30, 22, 45] 
}
df = pd.DataFrame(data)

# --- TIME-SERIES DATASET ---
base_time = datetime(2025, 10, 28, 6, 0)
time_intervals = [base_time + timedelta(hours=i*3) for i in range(6)]
time_data = []
for district in ['Kakinada', 'Konaseema', 'East Godavari', 'West Godavari']:
    max_wind_val = df.loc[df['District'] == district, 'Max_WindSpeed_kmph'].values
    if max_wind_val.size > 0:
        max_wind = max_wind_val[0]
        wind_progression = [max_wind*0.3, max_wind*0.7, max_wind*1.0, max_wind*0.8, max_wind*0.5, max_wind*0.2]
        for i, timestamp in enumerate(time_intervals):
            time_data.append({
                'District': district,
                'Timestamp': timestamp,
                'Reported_Wind_Speed_kmph': wind_progression[i]
            })
df_time_series = pd.DataFrame(time_data)

# --- Function to convert dataframe to CSV ---
@st.cache_data
def convert_df_to_csv(df):
    return df.to_csv(index=False).encode('utf-8')

csv_data = convert_df_to_csv(df)

# --- HEADER ---
st.title("🌪️ Cyclone Montha: Andhra Pradesh Advanced Dashboard")
st.markdown("""
This dashboard provides a comprehensive overview of the impact of **Cyclone Montha** on various districts in Andhra Pradesh. 
It tracks key metrics from storm intensity to the ongoing relief and recovery efforts.
""")
last_updated_time = datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
st.markdown(f"**Last Updated:** `{last_updated_time} (IST)`")


# --- SIDEBAR ---
st.sidebar.header("Dashboard Tools & Filters")

# --- NEW: UI Settings (Dark Mode Toggle) ---
st.sidebar.subheader("🎨 UI Settings")
# Use session state to remember the toggle's value
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False # Default to light

use_dark_charts = st.sidebar.toggle("Enable Dark Mode Charts", key='dark_mode')
# Set Plotly theme based on the toggle
plotly_theme = "plotly_dark" if use_dark_charts else "plotly"


# --- NEW: Reorganized Tools into an Expander ---
with st.sidebar.expander("📊 Analysis Tools", expanded=True):
    # --- TOOL 1: DISTRICT SPOTLIGHT ---
    district_list = ["None"] + sorted(df['District'].unique())
    spotlight_district = st.selectbox(
        "Select District for Spotlight",
        options=district_list
    )

    # --- TOOL 2: THRESHOLD SLIDER ---
    rainfall_threshold = st.slider(
        "Filter by Minimum Rainfall (mm)",
        min_value=0,
        max_value=int(df['Total_Rainfall_mm'].max()),
        value=0,
        step=10
    )

# --- Original Filter ---
st.sidebar.subheader("District Multi-Select")
st.sidebar.markdown("Select districts to display on charts:")
selected_districts = st.sidebar.multiselect(
    'Districts',
    options=df['District'].unique(),
    default=df['District'].unique(),
    label_visibility="collapsed" # Hides the 'Districts' label
)

# --- Download & Data Source ---
st.sidebar.markdown("---")
st.sidebar.download_button(
    label="📥 Download Full Data (CSV)",
    data=csv_data,
    file_name='cyclone_montha_impact_data.csv',
    mime='text/csv',
)
st.sidebar.info(
    "**Data Source:** Simulated data based on IMD reports and "
    "APSDMA bulletins."
)

# --- MAIN DASHBOARD ---

# --- NEW FILTERING LOGIC ---
df_multiselect = df[df['District'].isin(selected_districts)]
df_filtered = df_multiselect[df_multiselect['Total_Rainfall_mm'] >= rainfall_threshold]
df_time_series_filtered = df_time_series[df_time_series['District'].isin(selected_districts)]

# --- SPOTLIGHT BOX LOGIC ---
if spotlight_district != "None":
    st.subheader(f"📍 Spotlight on: {spotlight_district}")
    district_data = df[df['District'] == spotlight_district].iloc[0]
    
    scol1, scol2, scol3, scol4 = st.columns(4)
    scol1.metric("Max Wind (km/h)", f"{district_data['Max_WindSpeed_kmph']} km/h")
    scol2.metric("Total Rainfall (mm)", f"{district_data['Total_Rainfall_mm']} mm")
    scol3.metric("People Evacuated", f"{district_data['Evacuated_People']:,}")
    scol4.metric("Shelters Setup", f"{district_data['Shelters_Setup']}")
    
    scol5, scol6, scol7, scol8 = st.columns(4)
    scol5.metric("Power Resumed", f"{district_data['Power_Resumed_%']}%")
    scol6.metric("Comms Resumed", f"{district_data['Comms_Resumed_%']}%")
    scol7.metric("Food Packets", f"{district_data['Food_Packets']:,}")
    scol8.metric("Medical Teams", f"{district_data['Medical_Teams']}")
    st.markdown("---")

# Check if the final filtered dataframe is empty
if df_filtered.empty:
    st.warning("No districts match your current filter settings (Multi-select and/or Rainfall slider).")
else:
    # --- KEY METRICS ---
    total_evacuated = int(df_filtered['Evacuated_People'].sum())
    total_shelters = int(df_filtered['Shelters_Setup'].sum())
    total_food_packets = int(df_filtered['Food_Packets'].sum())

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Evacuated (from selection)", f"{total_evacuated:,}")
    col2.metric("Total Shelters (from selection)", f"{total_shelters:,}")
    col3.metric("Food Packets (from selection)", f"{total_food_packets:,}")
    
    st.markdown("---")

    # --- NEW: Updated Tab Icons ---
    tab1, tab2, tab3 = st.tabs(["🗺️ Overview & Evacuation", "📈 Impact Over Time", "🤝 Relief & Recovery"])

    with tab1:
        st.header("Overview & Evacuation Status")
        
        most_rain_district = df_filtered.loc[df_filtered['Total_Rainfall_mm'].idxmax()]
        most_evac_district = df_filtered.loc[df_filtered['Evacuated_People'].idxmax()]
        
        st.info(
            f"**Key Insights (for current selection):**\n"
            f"* **Highest Rainfall:** {most_rain_district['District']} ({most_rain_district['Total_Rainfall_mm']:,} mm)\n"
            f"* **Largest Evacuation:** {most_evac_district['District']} ({most_evac_district['Evacuated_People']:,} people)"
        )

        col4, col5 = st.columns([1, 2])
        
        with col4:
            st.subheader("Impacted Districts")
            df_map = df_filtered.rename(columns={'lat': 'latitude', 'lon': 'longitude'})
            st.map(df_map[['latitude', 'longitude']], zoom=6)

        with col5:
            st.subheader("Evacuation Scale by District")
            fig_evac = px.treemap(df_filtered, 
                                 path=[px.Constant("All Districts"), 'Alert_Level', 'District'], 
                                 values='Evacuated_People',
                                 color='District',
                                 title='Total Evacuees by District and Alert Level',
                                 template=plotly_theme # Apply theme
                                )
            fig_evac.update_traces(textinfo="label+value+percent root")
            st.plotly_chart(fig_evac, use_container_width=True)

    with tab2:
        st.header("Storm Impact Analysis (Wind & Rain)")
        
        st.subheader("Storm Progression: Wind Speed Over Time")
        if not df_time_series_filtered.empty:
            fig_time = px.line(df_time_series_filtered,
                               x='Timestamp',
                               y='Reported_Wind_Speed_kmph',
                               color='District',
                               markers=True,
                               title='Reported Wind Speed (km/h) as Storm Progresses',
                               template=plotly_theme # Apply theme
                               )
            fig_time.update_xaxes(title="Time (Oct 28, 2025)")
            st.plotly_chart(fig_time, use_container_width=True)
        else:
            st.info("No detailed time-series data for the selected district(s).")
            
        st.markdown("---")

        st.subheader("Total Rainfall by District (mm)")
        fig_rain = px.bar(df_filtered, 
                          x='District', 
                          y='Total_Rainfall_mm', 
                          color='Alert_Level',
                          title='Total Rainfall Intensity by District',
                          text='Total_Rainfall_mm',
                          color_discrete_map={
                              'Red': '#FF4B4B',
                              'Orange': '#FFA500',
                              'Yellow': '#FFD700'
                          },
                          template=plotly_theme # Apply theme
                          )
        fig_rain.update_traces(textposition='outside')
        st.plotly_chart(fig_rain, use_container_width=True)
        
    with tab3:
        st.header("Relief Efforts & Recovery Status")
        
        st.subheader("Recovery Status: Power vs. Communications")
        df_recovery = df_filtered.melt(id_vars=['District'], 
                                     value_vars=['Power_Resumed_%', 'Comms_Resumed_%'],
                                     var_name='Recovery_Type', 
                                     value_name='Percentage')
        
        fig_recovery = px.bar(df_recovery,
                            x='District',
                            y='Percentage',
                            color='Recovery_Type',
                            barmode='group',
                            title='Power and Comms Restoration (%) by District',
                            text='Percentage',
                            template=plotly_theme # Apply theme
                            )
        fig_recovery.update_yaxes(range=[0, 100])
        fig_recovery.update_traces(textposition='outside')
        st.plotly_chart(fig_recovery, use_container_width=True)
        
        st.markdown("---")
        
        st.subheader("Relief Supplies Distributed")
        df_relief = df_filtered.melt(id_vars=['District'], 
                                     value_vars=['Food_Packets', 'Water_Litres'],
                                     var_name='Supply_Type', 
                                     value_name='Quantity')
        
        fig_relief = px.bar(df_relief,
                            x='District',
                            y='Quantity',
                            color='Supply_Type',
                            barmode='group',
                            title='Food & Water Distribution by District',
                            template=plotly_theme # Apply theme
                            )
        st.plotly_chart(fig_relief, use_container_width=True)
        
        st.markdown("---")
        
        st.subheader("Impact vs. Recovery: Rainfall vs. Power")
        fig_scatter = px.scatter(df_filtered, 
                                 x='Total_Rainfall_mm', 
                                 y='Power_Resumed_%', 
                                 size='Max_WindSpeed_kmph',
                                 color='Alert_Level',
                                 hover_name='District',
                                 title='Rainfall vs. Power Resumption Efficiency (%)',
                                 color_discrete_map={
                                     'Red': '#FF4B4B',
                                     'Orange': '#FFA500',
                                     'Yellow': '#FFD700'
                                 },
                                 template=plotly_theme # Apply theme
                                 )
        fig_scatter.update_xaxes(title="Total Rainfall (mm)")
        fig_scatter.update_yaxes(title="Power Resumed (%)")
        st.plotly_chart(fig_scatter, use_container_width=True)

    # --- RAW DATA TABLE (FIX APPLIED) ---
    with st.expander("View Full Raw Data for Filtered Districts"):
        # This line is now fixed to avoid the 'matplotlib' error.
        # It will display a standard table without the color gradients.
        st.dataframe(df_filtered)


