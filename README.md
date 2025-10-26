# The Big Bank Theory - Simple Multiplayer Game

A completely simple web app without passwords. Just dice rolling and admin control.

## ✅ What This Does

- **No passwords** - Anyone can access
- **Simple dice rolling** - Players roll dice and see results
- **Admin controls** - Admin can adjust balances, move teams, give properties
- **Real-time updates** - Everyone sees changes instantly
- **No refresh issues** - Clean, simple implementation

## 🚀 How to Run

```bash
cd simple_game
pip install streamlit
streamlit run app.py
```

Access at: http://localhost:8501

## 🎮 How It Works

### For Players:
1. **See current turn** - Who's turn it is
2. **See dice roll** - When someone rolls dice
3. **See all teams** - Everyone's balance and position
4. **No login needed** - Just open the page

### For Admin:
1. **Roll dice** - Click "Roll Dice" for current team
2. **End turn** - Click "End Turn" to move to next team
3. **Adjust balances** - Give or take money from teams
4. **Move teams** - Change team positions manually
5. **Give properties** - Assign properties to teams
6. **Save/Load** - Save game state

## 🏦 Game Features

- **5 Teams** with different colors
- **24 Properties** on the board
- **Dice rolling** with movement
- **Balance tracking** for each team
- **Position tracking** for each team
- **Property ownership** system

## 🎯 Admin Controls

### Balance Management:
- Select team
- Enter amount (positive or negative)
- Click "Adjust Balance"

### Position Management:
- Select team
- Enter new position (0-23)
- Click "Move Team"

### Property Management:
- Select team
- Select property
- Click "Give Property"

### Game Management:
- **Roll Dice** - Roll for current team
- **End Turn** - Move to next team
- **Reset Game** - Start over
- **Save Game** - Save current state
- **Load Game** - Load saved state

## 📱 Streamlit Cloud Deployment

1. **Create GitHub repository**
2. **Upload `app.py` and `requirements.txt`**
3. **Go to [share.streamlit.io](https://share.streamlit.io)**
4. **Deploy with main file: `app.py`**
5. **Share URL with participants**

## 🎮 Game Flow

1. **Admin opens** the page
2. **Players watch** the screen (or open on their devices)
3. **Admin clicks "Roll Dice"** for current team
4. **Everyone sees** the dice result
5. **Admin can adjust** balances, positions, properties
6. **Admin clicks "End Turn"** to move to next team
7. **Repeat** for all teams

## 💡 Key Benefits

- ✅ **No passwords** - Easy access
- ✅ **No refresh issues** - Clean implementation
- ✅ **Real-time updates** - Everyone sees changes
- ✅ **Admin control** - Full control over game
- ✅ **Simple interface** - Easy to use
- ✅ **Streamlit Cloud ready** - Deploy anywhere

## 🎯 Best Practices

### For Admin:
- **Roll dice** for each team in turn
- **Adjust balances** as needed
- **Give properties** when appropriate
- **Save game** regularly
- **Communicate** with players

### For Players:
- **Watch the screen** for updates
- **See your balance** and position
- **Wait for your turn**
- **No action needed** - admin controls everything

## 🚀 Ready to Use!

This is the **simplest possible** implementation:

- **No passwords** - Just open and play
- **No refresh issues** - Clean code
- **Admin control** - Full game control
- **Real-time updates** - Everyone sees changes
- **Easy deployment** - One file solution

Perfect for events where you want simple, reliable gameplay!

---

**The Big Bank Theory - Simple Version** 🏦

**No passwords, no refresh issues, just simple fun!**
