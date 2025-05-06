import subprocess
from typing import Any

from kitty.boss import Boss
from kitty.window import Window

EnglishLanguageIndex = 0
LanguageIndexBeforeFocus = -1
# def on_load(boss: Boss, data: dict[str, Any]) -> None:
#     # This is a special function that is called just once when this watcher
#     # module is first loaded, can be used to perform any initializztion/one
#     # time setup. Any exceptions in this function are printed to kitty's
#     # STDERR but otherwise ignored.
#     ...
#
# def on_resize(boss: Boss, window: Window, data: dict[str, Any]) -> None:
#     # Here data will contain old_geometry and new_geometry
#     # Note that resize is also called the first time a window is created
#     # which can be detected as old_geometry will have all zero values, in
#     # particular, old_geometry.xnum and old_geometry.ynum will be zero.
#     ...


def on_focus_change(boss: Boss, window: Window, data: dict[str, Any]) -> None:
    global LanguageIndexBeforeFocus  # Declare global inside the function
    global EnglishLanguageIndex  # Declare global inside the function
    # Extract the new title from data
    # Log for debugging (optional)
    try:
        focused = data.get("focused", False)
        result_current_language = subprocess.run(["/home/andrei/.scripts/plasma/layout-current-get.sh"], check=True, capture_output = True, text = True)
        layout_result = result_current_language.stdout.strip()  # Get the layout, strip extra spaces
        layout_index = int(layout_result)
        # subprocess.run([
        #     "notify-send",
        #     "--app-name=Kitty",
        #     "--urgency=normal",
        #     # summary,
        #     f"Current:{layout_index}"
        #     # body
        #     # flat_data
        # ], check=True)
        if focused:
            if layout_index != 0:
                LanguageIndexBeforeFocus = layout_index
                # subprocess.run(["/home/andrei/.scripts/plasma/layout-current-set.sh", f"{EnglishLanguageIndex}"], check=True)
                subprocess.run(["/home/andrei/.scripts/plasma/layout-current-set.sh", "0"], check=True)
                # print(f"Kitty focused. Language was {result_current_language.returncode} switching to English") 
            else:
                LanguageIndexBeforeFocus = 0
        else:        
            if LanguageIndexBeforeFocus > 0:
                switch_result = subprocess.run(["/home/andrei/.scripts/plasma/layout-current-set.sh", f"{LanguageIndexBeforeFocus}"], check=True)
                # print(f"Kitty language was {result.returncode} switching to {switch_result.result}") 
    except subprocess.CalledProcessError as e:
        print(f"Error running script: {e}")
    except FileNotFoundError:
        print(f"Script not found: {script_path}")

# def on_close(boss: Boss, window: Window, data: dict[str, Any])-> None:
#     # called when window is closed, typically when the program running in
#     # it exits
#     ...
#
# def on_set_user_var(boss: Boss, window: Window, data: dict[str, Any]) -> None:
#     # called when a "user variable" is set or deleted on a window. Here
#     # data will contain key and value
#     ...
#
# def on_title_change(boss: Boss, window: Window, data: dict[str, Any]) -> None:
#     # called when the window title is changed on a window. Here
#     # data will contain title and from_child. from_child will be True
#     # when a title change was requested via escape code from the program
#     # running in the terminal
#     ...
#
# def on_cmd_startstop(boss: Boss, window: Window, data: dict[str, Any]) -> None:
#     # called when the shell starts/stops executing a command. Here
#     # data will contain is_start, cmdline and time.
#     ...
#
# def on_color_scheme_preference_change(boss: Boss, window: Window, data: dict[str, Any]) -> None:
#     # called when the color scheme preference of this window changes from
#     # light to dark or vice versa. data contains is_dark and via_escape_code
#     # the latter will be true if the color scheme was changed via escape
#     # code received from the program running in the window
#     ...
