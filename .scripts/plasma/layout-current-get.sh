#!/bin/bash
echo $(qdbus org.kde.keyboard /Layouts org.kde.KeyboardLayouts.getLayout)
