"""
The Big Bank Theory - Clean Multiplayer Game
Simple, working implementation without refresh issues
"""
import streamlit as st
import json
import os
import random
from datetime import datetime
from typing import Dict, List, Optional

# Game configuration
PASSWORDS = {
    "ADMIN": "admin123",
    "T1": "team1", "T2": "team2", "T3": "team3", "T4": "team4", "T5": "team5"
}

USER_TYPES = {
    "ADMIN": "Admin Panel",
    "T1": "Team 1", "T2": "Team 2", "T3": "Team 3", "T4": "Team 4", "T5": "Team 5"
}

# Game state file
GAME_STATE_FILE = "game_state.json"

def init_session_state():
    """Initialize session state"""
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
        st.session_state.user_type = None
        st.session_state.game_state = create_initial_game_state()

def create_initial_game_state():
    """Create initial game state"""
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
        'actions': [],
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

def add_action(action_type: str, team_id: str, params: dict = None):
    """Add action to queue"""
    action = {
        'id': f"{team_id}_{datetime.now().timestamp()}",
        'type': action_type,
        'team_id': team_id,
        'params': params or {},
        'timestamp': datetime.now().isoformat(),
        'status': 'pending'
    }
    st.session_state.game_state['actions'].append(action)
    save_game_state()
    return action['id']

def get_pending_actions():
    """Get pending actions"""
    return [a for a in st.session_state.game_state['actions'] if a['status'] == 'pending']

def approve_action(action_id: str):
    """Approve and execute action"""
    for action in st.session_state.game_state['actions']:
        if action['id'] == action_id:
            action['status'] = 'approved'
            execute_action(action)
            save_game_state()
            return True
    return False

def reject_action(action_id: str):
    """Reject action"""
    for action in st.session_state.game_state['actions']:
        if action['id'] == action_id:
            action['status'] = 'rejected'
            save_game_state()
            return True
    return False

def execute_action(action):
    """Execute approved action"""
    game_state = st.session_state.game_state
    team_id = action['team_id']
    team = next(t for t in game_state['teams'] if t['id'] == team_id)
    
    if action['type'] == 'roll_dice':
        dice = random.randint(1, 6)
        game_state['dice_roll'] = dice
        new_pos = (team['position'] + dice) % 24
        if team['position'] + dice >= 24:
            team['balance'] += 2000000
        team['position'] = new_pos
        
    elif action['type'] == 'buy_property':
        prop_index = action['params'].get('property_index', team['position'])
        prop = game_state['properties'][prop_index]
        if prop['owner'] is None and team['balance'] >= prop['price']:
            team['balance'] -= prop['price']
            prop['owner'] = team_id
            
    elif action['type'] == 'sell_property':
        prop_index = action['params'].get('property_index')
        prop = game_state['properties'][prop_index]
        if prop['owner'] == team_id:
            refund = prop['price'] // 2
            team['balance'] += refund
            prop['owner'] = None
            
    elif action['type'] == 'end_turn':
        game_state['current_team'] = (game_state['current_team'] + 1) % 5
        game_state['dice_roll'] = 0

def login_page():
    """Show login page"""
    st.title("🏦 The Big Bank Theory")
    st.markdown("---")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("### Login")
        user_type = st.selectbox("Select your role:", list(USER_TYPES.keys()), format_func=lambda x: USER_TYPES[x])
        password = st.text_input("Password:", type="password")
        
        if st.button("Login", use_container_width=True, type="primary"):
            if password == PASSWORDS.get(user_type):
                st.session_state.authenticated = True
                st.session_state.user_type = user_type
                st.success("Login successful!")
                st.rerun()
            else:
                st.error("❌ Incorrect password!")
        
        st.markdown("---")
        st.info("👥 Share this link with participants. Each team needs their password.")

def team_page(team_id: str):
    """Show team page"""
    game_state = st.session_state.game_state
    team = next(t for t in game_state['teams'] if t['id'] == team_id)
    current_team = game_state['teams'][game_state['current_team']]
    
    st.title(f"🏦 {team['name']} Control Panel")
    
    # Dice roll display
    if game_state['dice_roll'] > 0:
        if current_team['id'] == team_id:
            st.markdown(f"""
            <div style='background-color: #FFD700; color: black; padding: 20px; border-radius: 10px; margin-bottom: 20px; text-align: center; border: 3px solid #FFA500;'>
            <h1>🎲 DICE ROLLED: {game_state['dice_roll']} 🎲</h1>
            <p>You rolled a {game_state['dice_roll']}!</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div style='background-color: #E0E0E0; color: black; padding: 15px; border-radius: 10px; margin-bottom: 20px; text-align: center;'>
            <h3>🎲 {current_team['name']} rolled: {game_state['dice_roll']}</h3>
            </div>
            """, unsafe_allow_html=True)
    
    # Team info
    st.markdown(f"""
    <div style='background-color: {team['color']}; color: white; padding: 15px; border-radius: 10px; margin-bottom: 20px;'>
    <h2>Balance: ₹{team['balance']:,}</h2>
    <p>Position: {team['position']} | {game_state['properties'][team['position']]['name']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Action buttons
    st.markdown("### Action Center")
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🎲 Roll Dice", use_container_width=True, type="primary"):
            add_action("roll_dice", team_id)
            st.success("✅ Dice roll request sent to admin!")
        
        if st.button("✅ End Turn", use_container_width=True):
            if current_team['id'] == team_id:
                add_action("end_turn", team_id)
                st.success("✅ Turn end request sent to admin!")
            else:
                st.warning("⚠️ It's not your turn yet!")
    
    with col2:
        prop = game_state['properties'][team['position']]
        if prop['owner'] is None and prop['price'] > 0:
            if st.button(f"💰 Buy {prop['name']}", use_container_width=True):
                if team['balance'] >= prop['price']:
                    add_action("buy_property", team_id, {"property_index": team['position']})
                    st.success("✅ Buy property request sent to admin!")
                else:
                    st.error("❌ Insufficient balance!")
        
        if st.button("🏠 My Properties", use_container_width=True):
            owned = [p for p in game_state['properties'] if p['owner'] == team_id]
            if owned:
                for prop in owned:
                    st.write(f"• {prop['name']} - Rent: ₹{prop['rent']:,}")
            else:
                st.info("You don't own any properties yet")
    
    # Current property info
    st.markdown("---")
    st.subheader("📍 Current Position")
    prop = game_state['properties'][team['position']]
    st.markdown(f"**{prop['name']}**")
    if prop['price'] > 0:
        st.markdown(f"- Price: ₹{prop['price']:,}")
        st.markdown(f"- Rent: ₹{prop['rent']:,}")
        if prop['owner']:
            owner_team = next(t for t in game_state['teams'] if t['id'] == prop['owner'])
            st.markdown(f"- Owner: {owner_team['name']}")
    
    # Pending actions
    pending = [a for a in get_pending_actions() if a['team_id'] == team_id]
    if pending:
        st.markdown("---")
        st.subheader("⏳ Pending Actions")
        for action in pending:
            st.markdown(f"⏳ {action['type']} - Waiting for admin approval")

def admin_page():
    """Show admin page"""
    game_state = st.session_state.game_state
    
    st.title("🏦 Admin Control Panel")
    
    # Game controls
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("▶️ Start Game", use_container_width=True, type="primary"):
            game_state['game_started'] = True
            save_game_state()
            st.success("Game started!")
        
        if st.button("🔄 Reset Game", use_container_width=True):
            st.session_state.game_state = create_initial_game_state()
            save_game_state()
            st.success("Game reset!")
    
    with col2:
        if st.button("💾 Save Game", use_container_width=True):
            save_game_state()
            st.success("Game saved!")
    
    with col3:
        if st.button("🔄 Load Game", use_container_width=True):
            load_game_state()
            st.success("Game loaded!")
    
    # Current team display
    current_team = game_state['teams'][game_state['current_team']]
    st.markdown(f"""
    <div style='background-color: {current_team['color']}; color: white; padding: 15px; border-radius: 10px; margin-bottom: 20px;'>
    <h2>Current Turn: {current_team['name']}</h2>
    <p>Balance: ₹{current_team['balance']:,} | Position: {current_team['position']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Pending actions
    st.markdown("---")
    st.subheader("⏳ Pending Action Requests")
    
    pending_actions = get_pending_actions()
    
    if pending_actions:
        for action in pending_actions:
            team = next(t for t in game_state['teams'] if t['id'] == action['team_id'])
            
            with st.container():
                st.markdown(f"### {team['name']} - {action['type']}")
                st.markdown(f"**Parameters:** {action['params']}")
                st.markdown(f"*Requested at: {action['timestamp']}*")
                
                col1, col2, col3 = st.columns([1, 1, 2])
                
                with col1:
                    if st.button("✅ Approve", key=f"approve_{action['id']}", use_container_width=True):
                        if approve_action(action['id']):
                            st.success("Action approved and executed!")
                        else:
                            st.error("Failed to approve action")
                
                with col2:
                    if st.button("❌ Reject", key=f"reject_{action['id']}", use_container_width=True):
                        if reject_action(action['id']):
                            st.warning("Action rejected!")
                        else:
                            st.error("Failed to reject action")
                
                st.markdown("---")
    else:
        st.info("No pending actions")
    
    # All teams status
    st.markdown("---")
    st.subheader("👥 All Teams Status")
    
    cols = st.columns(5)
    for idx, team in enumerate(game_state['teams']):
        with cols[idx]:
            st.markdown(f"""
            <div style='border: 2px solid {team['color']}; padding: 10px; border-radius: 5px;'>
            <h4>{team['name']}</h4>
            <p>₹{team['balance']:,}</p>
            <p>Pos: {team['position']}</p>
            </div>
            """, unsafe_allow_html=True)

def main():
    """Main app function"""
    st.set_page_config(
        page_title="The Big Bank Theory",
        layout="wide",
        page_icon="🏦",
        initial_sidebar_state="collapsed"
    )
    
    # Initialize session state
    init_session_state()
    
    # Load game state
    load_game_state()
    
    # Check authentication
    if not st.session_state.authenticated:
        login_page()
        return
    
    # Hide default Streamlit elements
    hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    
    # Sidebar with logout
    with st.sidebar:
        st.markdown("### ⚙️ Controls")
        
        if st.button("🚪 Logout", use_container_width=True):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
        
        # Status info
        st.markdown("---")
        st.markdown("### 📊 Status")
        game_state = st.session_state.game_state
        current_team = game_state['teams'][game_state['current_team']]
        st.markdown(f"**Current Turn:** {current_team['name']}")
        st.markdown(f"**Dice Roll:** {game_state['dice_roll'] if game_state['dice_roll'] > 0 else 'None'}")
        st.markdown(f"**Pending Actions:** {len(get_pending_actions())}")
        
        # Instructions
        st.markdown("---")
        st.info("💡 **No auto-refresh** - Actions update instantly")
        st.markdown("🔄 **Manual control** - Click buttons to see updates")
    
    # Route to appropriate page
    user_type = st.session_state.user_type
    
    if user_type == "ADMIN":
        admin_page()
    elif user_type in ["T1", "T2", "T3", "T4", "T5"]:
        team_page(user_type)
    else:
        st.error("Invalid user type")

if __name__ == "__main__":
    main()
