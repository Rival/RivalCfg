#!/bin/bash

# Configuration
USE_REFERENCE_CLONE=true  # If true, makes a reflink copy instead of full copy

# Notification function
notify_info() {
    # Display an information notification
    notify-send "Info" "$1" --icon=dialog-information --urgency=normal
}

notify_success() {
    # Display a success notification
    notify-send "Success" "$1" --icon=dialog-ok --urgency=low
}

notify_error() {
    # Display an error notification
    notify-send "Error" "$1" --icon=dialog-error --urgency=critical
}

# Check for argument
if [ $# -eq 0 ]; then
    notify_error "Usage: $0 /path/to/repository"
    exit 1
fi

SOURCE_PATH="$1"

# Check if source exists
if [ ! -d "$SOURCE_PATH" ]; then
    notify_error "Directory '$SOURCE_PATH' does not exist."
    exit 1
fi

# Extract base repo name and parent path
REPO_NAME=$(basename "$SOURCE_PATH")
OUTER_REPO_PATH=$(dirname "$SOURCE_PATH")

# Find the next available clone name
COUNT=1
while [ -e "$OUTER_REPO_PATH/${REPO_NAME}${COUNT}" ]; do
    COUNT=$((COUNT + 1))
done

DEST_NAME="${REPO_NAME}${COUNT}"
DEST_PATH="$OUTER_REPO_PATH/$DEST_NAME"

# Notify about the cloning process
notify_info "Creating reflink copy of $SOURCE_PATH to $DEST_PATH..."

# Clone using reflink copy for Btrfs
if cp --reflink=always -r "$SOURCE_PATH" "$DEST_PATH"; then
    notify_success "Successfully created reflink clone: $DEST_NAME"
else
    notify_error "Failed to create reflink clone. Make sure:"
    notify_error "   - Filesystem is Btrfs (supports reflinks)"
    notify_error "   - 'cp' supports --reflink"
    exit 1
fi
