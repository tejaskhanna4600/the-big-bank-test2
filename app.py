"""
The Big Bank Theory - Simple Multiplayer Game
Fixed version with reliable auto-refresh and single-click buttons
"""
import streamlit as st
import json
import os
import random
from datetime import datetime
import time

# Game state file
GAME_STATE_FILE = "game_state.json"

def init_game_state():
    """Initialize game state"""
    return {
        'teams': [
            {'id': 'T1', 'name': 'Team 1', 'balance': 10000000, 'position': 0, 'color': '#D32F2F'},
            {'id': 'T2', 'name': 'Team 2', 'balance': 10000000, 'position': 0, 'color': '#1976D2'},
            {'id': 'T3', 'name': 'Team 3', 'balance': 10000000, 'position': 0, 'color': '#388E3C'},
            {'id': 'T4', 'name': 'Team 4', 'balance': 10000000, 'position': 0, 'color': '#F57C00'},
            {'id': 'T5', 'name': 'Team 5', 'balance': 10000000, 'position': 0, 'color': '#7B1FA2'},
        ],
        'current_team': 0,
        'dice_roll': 0,
        'properties': [
            {'name': 'START/GO', 'price': 0, 'rent': 0, 'owner': None},
            {'name': 'Digital Marketing', 'price': 2000000, 'rent': 500000, 'owner': None},
            {'name': 'MYSTERY WHEEL', 'price': 0, 'rent': 0, 'owner': None},
            {'name': 'Social Media', 'price': 2500000, 'rent': 600000, 'owner': None},
            {'name': 'CHANCE', 'price': 0, 'rent': 0, 'owner': None},
            {'name': 'Content Marketing', 'price': 2000000, 'rent': 500000, 'owner': None},
            {'name': 'Society Penalty', 'price': 0, 'rent': 0, 'owner': None},
            {'name': 'Email Marketing', 'price': 2500000, 'rent': 600000, 'owner': None},
            {'name': 'CHANCE', 'price': 0, 'rent': 0, 'owner': None},
            {'name': 'SEO', 'price': 3000000, 'rent': 800000, 'owner': None},
            {'name': 'MYSTERY WHEEL', 'price': 0, 'rent': 0, 'owner': None},
            {'name': 'PPC Advertising', 'price': 3500000, 'rent': 1000000, 'owner': None},
            {'name': 'Free Parking', 'price': 0, 'rent': 0, 'owner': None},
            {'name': 'Influencer Marketing', 'price': 3000000, 'rent': 800000, 'owner': None},
            {'name': 'MYSTERY WHEEL', 'price': 0, 'rent': 0, 'owner': None},
            {'name': 'Brand Management', 'price': 3500000, 'rent': 1000000, 'owner': None},
            {'name': 'CHANCE', 'price': 0, 'rent': 0, 'owner': None},
            {'name': 'Event Management', 'price': 2500000, 'rent': 600000, 'owner': None},
            {'name': 'Event Penalty', 'price': 0, 'rent': 0, 'owner': None},
            {'name': 'Market Research', 'price': 3000000, 'rent': 800000, 'owner': None},
            {'name': 'CHANCE', 'price': 0, 'rent': 0, 'owner': None},
            {'name': 'PR & Communications', 'price': 3500000, 'rent': 1000000, 'owner': None},
            {'name': 'MYSTERY WHEEL', 'price': 0, 'rent': 0, 'owner': None},
            {'name': 'Analytics', 'price': 2000000, 'rent': 500000, 'owner': None},
        ],
        'game_started': False
    }

def save_game_state():
    """Save game state to file"""
    with open(GAME_STATE_FILE, 'w') as f:
        json.dump(st.session_state.game_state, f, indent=2)

def load_game_state():
    """Load game state from file"""
    if os.path.exists(GAME_STATE_FILE):
        with open(GAME_STATE_FILE, 'r') as f:
            st.session_state.game_state = json.load(f)

def roll_dice():
    """Roll dice for current team"""
    game_state = st.session_state.game_state
    dice = random.randint(1, 6)
    game_state['dice_roll'] = dice
    
    # Move current team
    current_team = game_state['teams'][game_state['current_team']]
    new_pos = (current_team['position'] + dice) % 24
    
    # Check if passed GO
    if current_team['position'] + dice >= 24:
        current_team['balance'] += 2000000
    
    current_team['position'] = new_pos
    save_game_state()
    return dice

def next_turn():
    """Move to next team's turn"""
    game_state = st.session_state.game_state
    game_state['current_team'] = (game_state['current_team'] + 1) % 5
    game_state['dice_roll'] = 0
    save_game_state()

def main():
    """Main app function"""
    st.set_page_config(
        page_title="The Big Bank Theory",
        layout="wide",
        page_icon="🏦"
    )
    
    # Initialize session state
    if 'game_state' not in st.session_state:
        st.session_state.game_state = init_game_state()
    
    # Load game state
    load_game_state()
    
    game_state = st.session_state.game_state
    
    # Auto-refresh using meta tag
    st.markdown("""
    <meta http-equiv="refresh" content="3">
    """, unsafe_allow_html=True)
    
    # Title
    st.title("🏦 The Big Bank Theory")
    st.markdown("---")
    
    # Current team display
    current_team = game_state['teams'][game_state['current_team']]
    st.markdown(f"""
    <div style='background-color: {current_team['color']}; color: white; padding: 20px; border-radius: 10px; margin-bottom: 20px; text-align: center;'>
    <h1>Current Turn: {current_team['name']}</h1>
    <h2>Balance: ₹{current_team['balance']:,}</h2>
    <h3>Position: {current_team['position']} - {game_state['properties'][current_team['position']]['name']}</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Dice roll display
    if game_state['dice_roll'] > 0:
        st.markdown(f"""
        <div style='background-color: #FFD700; color: black; padding: 20px; border-radius: 10px; margin-bottom: 20px; text-align: center; border: 3px solid #FFA500;'>
        <h1>🎲 DICE ROLLED: {game_state['dice_roll']} 🎲</h1>
        <p>{current_team['name']} rolled a {game_state['dice_roll']}!</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Main controls
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🎲 Roll Dice", use_container_width=True, type="primary"):
            dice = roll_dice()
            st.success(f"🎲 {current_team['name']} rolled a {dice}!")
            st.rerun()
    
    with col2:
        if st.button("✅ End Turn", use_container_width=True):
            next_turn()
            st.success("Turn ended!")
            st.rerun()
    
    with col3:
        if st.button("🔄 Reset Game", use_container_width=True):
            st.session_state.game_state = init_game_state()
            save_game_state()
            st.success("Game reset!")
            st.rerun()
    
    # All teams status
    st.markdown("---")
    st.subheader("👥 All Teams Status")
    
    cols = st.columns(5)
    for idx, team in enumerate(game_state['teams']):
        with cols[idx]:
            is_current = idx == game_state['current_team']
            border_color = "#FFD700" if is_current else team['color']
            border_width = "3px" if is_current else "2px"
            
            st.markdown(f"""
            <div style='border: {border_width} solid {border_color}; padding: 15px; border-radius: 10px; background-color: {team['color']}20;'>
            <h3 style='color: {team['color']}; margin: 0;'>{team['name']}</h3>
            <p style='margin: 5px 0; font-size: 18px; font-weight: bold;'>₹{team['balance']:,}</p>
            <p style='margin: 5px 0;'>Pos: {team['position']}</p>
            <p style='margin: 5px 0; font-size: 12px;'>{game_state['properties'][team['position']]['name']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Admin controls
    st.markdown("---")
    st.subheader("🎮 Admin Controls")
    
    # Manual balance adjustment
    st.markdown("#### 💰 Adjust Team Balance")
    admin_col1, admin_col2, admin_col3 = st.columns(3)
    
    with admin_col1:
        team_select = st.selectbox("Select Team:", [f"Team {i+1}" for i in range(5)])
        team_idx = int(team_select.split()[1]) - 1
    
    with admin_col2:
        amount = st.number_input("Amount (can be negative):", value=0, step=100000)
    
    with admin_col3:
        if st.button("💸 Adjust Balance", use_container_width=True):
            game_state['teams'][team_idx]['balance'] += amount
            save_game_state()
            st.success(f"Balance adjusted by ₹{amount:,}")
            st.rerun()
    
    # Manual position adjustment
    st.markdown("#### 📍 Move Team Position")
    pos_col1, pos_col2, pos_col3 = st.columns(3)
    
    with pos_col1:
        pos_team_select = st.selectbox("Select Team:", [f"Team {i+1}" for i in range(5)], key="pos_team")
        pos_team_idx = int(pos_team_select.split()[1]) - 1
    
    with pos_col2:
        new_position = st.number_input("New Position:", min_value=0, max_value=23, value=0)
    
    with pos_col3:
        if st.button("🚀 Move Team", use_container_width=True):
            game_state['teams'][pos_team_idx]['position'] = new_position
            save_game_state()
            st.success(f"Moved to position {new_position}")
            st.rerun()
    
    # Property management
    st.markdown("#### 🏠 Give Property to Team")
    prop_col1, prop_col2, prop_col3 = st.columns(3)
    
    with prop_col1:
        prop_team_select = st.selectbox("Select Team:", [f"Team {i+1}" for i in range(5)], key="prop_team")
        prop_team_idx = int(prop_team_select.split()[1]) - 1
    
    with prop_col2:
        property_select = st.selectbox("Select Property:", 
                                     [f"{i}: {prop['name']}" for i, prop in enumerate(game_state['properties']) if prop['price'] > 0])
        prop_idx = int(property_select.split(':')[0])
    
    with prop_col3:
        if st.button("🏠 Give Property", use_container_width=True):
            if game_state['properties'][prop_idx]['owner'] is None:
                game_state['properties'][prop_idx]['owner'] = game_state['teams'][prop_team_idx]['id']
                save_game_state()
                st.success(f"Gave {game_state['properties'][prop_idx]['name']} to {game_state['teams'][prop_team_idx]['name']}")
                st.rerun()
            else:
                st.error("Property already owned!")
    
    # Game state info
    st.markdown("---")
    st.subheader("📊 Game State")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("💾 Save Game", use_container_width=True):
            save_game_state()
            st.success("Game saved!")
            st.rerun()
    
    with col2:
        if st.button("🔄 Load Game", use_container_width=True):
            load_game_state()
            st.success("Game loaded!")
            st.rerun()
    
    with col3:
        st.markdown(f"**Current Turn:** {game_state['current_team'] + 1}")
        st.markdown(f"**Dice Roll:** {game_state['dice_roll'] if game_state['dice_roll'] > 0 else 'None'}")
    
    # Auto-refresh status
    st.markdown("---")
    st.info("🔄 **Auto-refresh:** Every 3 seconds | **Manual:** Click buttons for instant updates")
    
    # Properties owned by teams
    st.markdown("---")
    st.subheader("🏠 Properties Owned")
    
    for team in game_state['teams']:
        owned_props = [prop for prop in game_state['properties'] if prop['owner'] == team['id']]
        if owned_props:
            st.markdown(f"**{team['name']}:** {', '.join([prop['name'] for prop in owned_props])}")
        else:
            st.markdown(f"**{team['name']}:** No properties owned")

if __name__ == "__main__":
    main()