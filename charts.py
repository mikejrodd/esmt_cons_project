import streamlit as st
import plotly.graph_objects as go

# Set page config for full-screen width
st.set_page_config(layout="wide")

# Sidebar layout
with st.sidebar:
    st.title("Incubator/Accelerator Competitive Analysis")
    
    # Selector buttons for app view
    app_selection = st.radio(
        "Select an analysis to view:",
        [
            "View comparison of higher-level competitor groups",
            "Compare Bayer within its cluster of similar competitors"
        ],
        index=0
    )
    
    st.markdown("---")
    
    if app_selection == "View comparison of higher-level competitor groups":
        st.subheader("Select clusters to compare")
        cluster_data = {
            "Corporate-Backed": {"Physical and Admin": 8, "Mentoring": 10, "Global Reach": 9, "Funding": 4, "Expertise": 8, "Local": 4},
            "Public/Academic-Funded": {"Physical and Admin": 7, "Mentoring": 8, "Global Reach": 4, "Funding": 6, "Expertise": 9, "Local": 9},
            "Science/Tech Parks": {"Physical and Admin": 10, "Mentoring": 6, "Global Reach": 7, "Funding": 9, "Expertise": 9, "Local": 10},
            "Private Co-Working": {"Physical and Admin": 9, "Mentoring": 6, "Global Reach": 7, "Funding": 6, "Expertise": 6, "Local": 8},
            "Venture-Driven": {"Physical and Admin": 6, "Mentoring": 9, "Global Reach": 9, "Funding": 10, "Expertise": 8, "Local": 6},
            "Non-Profit Aggregators": {"Physical and Admin": 2, "Mentoring": 10, "Global Reach": 10, "Funding": 5, "Expertise": 8, "Local": 6},
            "Bayer Co.Lab Berlin": {"Physical and Admin": 10, "Mentoring": 9, "Global Reach": 8, "Funding": 5, "Expertise": 8, "Local": 6},
        }
        
        all_clusters = list(cluster_data.keys())
        selected_clusters = st.multiselect("Select clusters to compare", options=all_clusters, default=all_clusters[:2])
        
        st.markdown("---")
        st.markdown("""
            ### More Information  
            High-level competitor groups were created based on secondary research, clustered using K-Means and Semantic analysis of group notes and competitor website material.  

            **See our** [Competitor Clusters Document](https://docs.google.com/document/d/1-oHKxNdkiebwOsY7FGmFCQzZrLf8G1pDUBTlOwcM4cA/edit?usp=sharing) **for details on the original 30 competitors included.**
        """)

    else:
        st.subheader("Select incubators to display")
        incubators = {
            "Bayer Co.Lab": [5, 9, 9, 9, 9, 10, 9, 6],
            "J Labs": [5, 8, 8, 7, 9, 10, 10, 7],
            "BioMedX": [8, 10, 4, 3, 8, 9, 6, 8],
            "BaseLaunch": [9, 9, 8, 8, 10, 7, 7, 9],
            "BioLabs": [3, 6, 5, 5, 6, 10, 8, 9],
            "BioInnovation Inst.": [10, 7, 8, 8, 7, 9, 6, 8],
        }
        
        selected_incubators = st.multiselect("Select incubators to display", list(incubators.keys()), default=list(incubators.keys())[:1])
        
        st.markdown("---")
        st.markdown("""
            ### More Information  
            Companies displayed are within the grouping of competitors similar to Bayer Co.Lab in existing value proposition.  

            **See our** [Final Close Competition Report](https://docs.google.com/document/d/1Hq2kWrcM_S5EvwDvBpE26Sr_NizTrHhqAgf0tBfFOV4/edit?usp=sharing) **for details on the companies displayed here and their likely stregths and weaknesses within the Wave 2 Value Proposition categories.**
        """)
# Main chart area
st.markdown("<div style='margin-left: 250px;'>", unsafe_allow_html=True)

fig = go.Figure()
if app_selection == "View comparison of higher-level competitor groups":
    categories = ["Physical and Admin", "Mentoring", "Global Reach", "Funding", "Expertise", "Local"]
    cluster_colors = {"Corporate-Backed": "#1f77b4", "Public/Academic-Funded": "#ff7f0e", "Science/Tech Parks": "#2ca02c", "Private Co-Working": "#d62728", "Venture-Driven": "#9467bd", "Non-Profit Aggregators": "#8c564b"}
    
    for cluster_name in selected_clusters:
        ratings = [cluster_data[cluster_name][cat] for cat in categories]
        fig.add_trace(go.Scatterpolar(r=ratings + [ratings[0]], theta=categories + [categories[0]], fill='toself', name=cluster_name, line=dict(color=cluster_colors.get(cluster_name, "#17becf"), width=3)))

else:
    categories = ["Funding Support", "Scientific Expertise", "Commercial & Regulatory", "Scaling & Business Mentorship", "Biopharma Partnerships", "Lab Space & Administration", "Global Network Development", "Local Network Development"]
    colors = ["red", "blue", "green", "purple", "orange", "cyan"]
    
    for i, name in enumerate(selected_incubators):
        values = incubators[name]
        fig.add_trace(go.Scatterpolar(r=values + [values[0]], theta=categories + [categories[0]], fill='toself', name=name, line=dict(color=colors[i % len(colors)], width=3)))

fig.update_layout(
    polar=dict(radialaxis=dict(visible=True, range=[0, 10])),
    showlegend=True,
    legend=dict(orientation="h", x=0.5, y=1.1, xanchor="center", yanchor="bottom"),
    width=1200,
    height=800,
    margin=dict(l=80, r=80, t=100, b=80)
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)
