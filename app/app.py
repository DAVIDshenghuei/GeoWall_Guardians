import streamlit as st
import folium
from streamlit_folium import folium_static
from datetime import datetime, timedelta

# Set page config (must be the first Streamlit command)
st.set_page_config(
    layout="wide",
    page_title="GeoWall Guardians",
    page_icon="🌍"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .stButton>button {
        width: 100%;
        background-color: #2e7d32;
        color: white;
        border: none;
        padding: 0.5rem;
        border-radius: 5px;
    }
    .stButton>button:hover {
        background-color: #1b5e20;
    }
    h1 {
        color: #1b5e20;
        text-align: center;
        padding: 0.5rem 0;
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }
    h3 {
        color: #2e7d32;
        padding: 0.3rem 0;
        font-size: 1.1rem;
        margin: 0;
    }
    .stSelectbox label, .stDateInput label, .stNumberInput label {
        color: #2e7d32;
        font-weight: bold;
        margin-bottom: 0.2rem;
    }
    div[data-testid="stVerticalBlock"] > div {
        padding: 0.2rem 0;
    }
    hr {
        margin: 0.5rem 0;
    }
    .element-container {
        margin-bottom: 0.5rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Title
st.title("GeoWall Guardians")

# Create two columns for the main content
col1, col2 = st.columns([1, 3])

with col1:
    # Create a container for better visual organization
    with st.container():
        st.subheader("🗓️ Time Range")
        start_date = st.date_input("Start Date", datetime.now() - timedelta(days=30))
        end_date = st.date_input("End Date", datetime.now(), min_value=start_date)
        
        if start_date > end_date:
            st.error("⚠️ Start date must be before end date")
    
    st.markdown("---")
    
    with st.container():
        st.subheader("⚙️ Parameters")
        temporal_step = st.number_input("Temporal Step (days)", 
                                      min_value=1, 
                                      max_value=60, 
                                      value=30,
                                      help="Number of days between each analysis")
        
        confidence_threshold = st.slider("Confidence Threshold", 
                                       0.0, 1.0, 0.5, 0.1,
                                       help="Minimum confidence level for predictions")
    
    st.markdown("---")
    
    with st.container():
        st.subheader("🎯 Mask Settings")
        col_mask1, col_mask2 = st.columns(2)
        with col_mask1:
            mask_cloud = st.checkbox("Mask Clouds", value=True)
        with col_mask2:
            mask_water = st.checkbox("Mask Water", value=True)
    
    st.markdown("---")
    
    # Run analysis button
    if st.button("🚀 Run Analysis"):
        if start_date > end_date:
            st.error("⚠️ Please fix the date range before running analysis")
        else:
            with st.spinner("Running analysis..."):
                st.success("✅ Analysis complete!")

with col2:
    # Region selection in a more compact form
    regions = {
        "East Africa": {"center": [5.0, 35.0]},
        "West Africa": {"center": [12.0, 0.0]},
        "North Africa": {"center": [25.0, 15.0]},
        "Middle East": {"center": [25.0, 45.0]}
    }
    
    selected_region = st.selectbox("🌍 Select Region", list(regions.keys()))
    region_center = regions[selected_region]["center"]
    
    # Create a base map centered on the selected region
    m = folium.Map(
        location=region_center,
        zoom_start=4,
        width='100%',
        control_scale=True
    )
    
    # Add tile layers with attribution
    folium.TileLayer(
        'OpenStreetMap',
        attr='© OpenStreetMap contributors'
    ).add_to(m)
    
    folium.TileLayer(
        'Stamen Terrain',
        attr='Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under ODbL.'
    ).add_to(m)
    
    # Add layer control
    folium.LayerControl().add_to(m)
    
    # Display the map
    folium_static(m, width=1000)

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #2e7d32; padding: 1rem 0;'>
        GeoWall Guardians | Powered by AI 🤖
    </div>
    """,
    unsafe_allow_html=True
)

