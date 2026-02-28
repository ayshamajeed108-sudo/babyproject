import streamlit as st
import pandas as pd
import json
import random
import os

# --- DATA GENERATION FUNCTION ---
def generate_safety_data(total_records=1000):
    brands = ["NordicKids", "Guardian", "EcoBaby", "SafeStep", "TinyTots", "PureSleep", "MamaEase", "BrightStarts"]
    categories = {
        "Sleep": {
            "items": ["Crib", "Bassinet", "Swaddle", "Crib Mattress", "Sleep Sack"],
            "ages": ["0-3 Months", "0-6 Months", "0-2 Years"],
            "hazards": ["Suffocation risk if loose bedding is used", "Positional asphyxia"],
            "standards": ["ASTM F1169", "CPSC 16 CFR"]
        },
        "Travel": {
            "items": ["Infant Car Seat", "Convertible Car Seat", "Stroller", "Baby Carrier"],
            "ages": ["0-12 Months", "0-4 Years", "4-10 Years"],
            "hazards": ["Improper harness tension", "Chest clip too low"],
            "standards": ["FMVSS 213", "ECE R44/04"]
        },
        "Toys": {
            "items": ["Silicone Teether", "Stacking Rings", "Plush Rattle", "Wooden Blocks"],
            "ages": ["3-12 Months", "6-18 Months", "12-36 Months"],
            "hazards": ["Choking hazard (small parts)", "Sharp edges if broken"],
            "standards": ["ASTM F963", "EN71"]
        },
        "Home Safety": {
            "items": ["Magnetic Cabinet Lock", "Furniture Strap", "Baby Gate", "Corner Guard"],
            "ages": ["6-24 Months", "1-3 Years", "All Ages"],
            "hazards": ["Failure of adhesive", "Incorrect installation height"],
            "standards": ["ASTM F1004", "RoHS"]
        }
    }

    dataset = []
    cat_list = list(categories.keys())
    for i in range(1, total_records + 1):
        cat_name = random.choice(cat_list)
        cat_data = categories[cat_name]
        brand = random.choice(brands)
        product_base = random.choice(cat_data["items"])
        status = random.choices(["Verified Safe", "Safety Alert", "Recall Active"], weights=[80, 15, 5])[0]
        
        entry = {
            "id": i,
            "product_name": f"{brand} {product_base}",
            "category": cat_name,
            "age_group": random.choice(cat_data["ages"]),
            "status": status,
            "safety_cert": random.choice(cat_data["standards"]),
            "primary_hazard": random.choice(cat_data["hazards"]) if status != "Verified Safe" else "None",
            "safety_tip": f"Always follow the manufacturer's manual for {product_base} setup.",
            "last_check_date": f"2026-{random.randint(1,2):02d}-{random.randint(1,28):02d}"
        }
        dataset.append(entry)
    
    return pd.DataFrame(dataset)

# --- STREAMLIT UI ---
st.set_page_config(page_title="Baby Product Safety Analyzer", page_icon="👶")

st.title("👶 Baby Product Safety Analyzer")
st.markdown("Generate safety datasets and analyze product risks instantly.")

# 1. Dataset Generation Section
if "df" not in st.session_state:
    st.session_state.df = None

if st.button("🔄 Generate/Reset Safety Dataset"):
    st.session_state.df = generate_safety_data(1000)
    st.success("Dataset generated with 1,000 records!")

# 2. Analysis Section (Only shown if data exists)
if st.session_state.df is not None:
    st.divider()
    df = st.session_state.df

    col1, col2 = st.columns(2)
    
    with col1:
        search_query = st.text_input("Enter Product Name (e.g., 'NordicKids'):")
    
    with col2:
        age_input = st.number_input("Enter Baby Age (Months):", min_value=0, max_value=120, value=6)

    if search_query:
        # Search filter
        results = df[df["product_name"].str.contains(search_query, case=False, na=False)]

        if not results.empty:
            product = results.iloc[0]
            
            st.subheader(f"🔍 Safety Analysis: {product['product_name']}")
            
            # Display Status with Color
            if product["status"] == "Verified Safe":
                st.success(f"**Status:** {product['status']}")
            elif product["status"] == "Safety Alert":
                st.warning(f"**Status:** {product['status']}")
            else:
                st.error(f"**Status:** {product['status']}")

            # Data Table/Metrics
            m_col1, m_col2 = st.columns(2)
            m_col1.write(f"**Category:** {product['category']}")
            m_col1.write(f"**Age Group:** {product['age_group']}")
            m_col1.write(f"**Certification:** {product['safety_cert']}")
            
            m_col2.write(f"**Primary Hazard:** {product['primary_hazard']}")
            m_col2.write(f"**Last Checked:** {product['last_check_date']}")
            
            st.info(f"💡 **Safety Tip:** {product['safety_tip']}")
            
            # Show similar products in the same category
            with st.expander("View Similar Products"):
                st.dataframe(results.head(10))
                
        else:
            st.error("❌ Product not found. Try a different brand or item name.")
    else:
        st.write("Enter a product name above to start the analysis.")
        
else:
    st.info("Please click the button above to generate the safety database.")