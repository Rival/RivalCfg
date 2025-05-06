#!/bin/bash

# Accept desired layout index as the first parameter
target_layout_index="$1"

# Get current layout index from KWin's D-Bus interface
current_layout_index=$(qdbus org.kde.keyboard /Layouts org.kde.KeyboardLayouts.getLayout)

# Get the layout list from KDE settings
layout_list=$(kreadconfig5 --file kxkbrc --group Layout --key LayoutList)

# Split layout list into array
IFS=',' read -ra layouts <<< "$layout_list"

if [ "$current_layout_index" -ne "$target_layout_index" ]; then
  qdbus org.kde.keyboard /Layouts org.kde.KeyboardLayouts.setLayout "$target_layout_index"
  echo "Switched to ${layouts[$target_layout_index]}"
else
  echo 0
fi
