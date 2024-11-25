#!/bin/bash
SESSION_NAME="dev"

# Check if the session already exists and kill it if it does
tmux has-session -t $SESSION_NAME 2>/dev/null
if [ $? == 0 ]; then
    tmux kill-session -t $SESSION_NAME
fi

# Create a new tmux session named 'dev'
tmux new-session -d -s $SESSION_NAME

# Create a new tmux session named 'dev'
tmux new-session -d -s dev

# Split the window into two panes
tmux split-window -h

# Select the first pane (left) and run the backend
tmux select-pane -t 0
tmux send-keys 'cd backend && direnv allow' C-m
tmux send-keys 'pdm run fastapi run app/main.py' C-m

# Select the second pane (right) and run the frontend
tmux select-pane -t 1
tmux send-keys 'cd frontend && pnpm run dev' C-m

# Attach to the tmux session
tmux attach-session -t dev