import pyray as pr
import raylib as rb

WINDOW_H = 800
WINDOW_W = 800

pr.init_window(WINDOW_H, WINDOW_W, "Doom clone")
pr.set_target_fps(60)

while not pr.window_should_close():
    pr.begin_drawing()
    pr.clear_background(pr.WHITE)
    if pr.is_key_down(rb.KEY_W) and pr.is_key_down(rb.KEY_M):
        print("Move up")
    if pr.is_key_down(rb.KEY_S) and pr.is_key_down(rb.KEY_M):
        print("Move down")
    if pr.is_key_down(rb.KEY_A) and pr.is_key_down(rb.KEY_M):
        print("Move left")
    if pr.is_key_down(rb.KEY_D) and pr.is_key_down(rb.KEY_M):
        print("Move right")
    if pr.is_key_down(rb.KEY_W) and not pr.is_key_down(rb.KEY_M):
        print("Up")
    if pr.is_key_down(rb.KEY_S) and  not pr.is_key_down(rb.KEY_M):
        print("Down")
    if pr.is_key_down(rb.KEY_A) and  not pr.is_key_down(rb.KEY_M):
        print("Left")
    if pr.is_key_down(rb.KEY_D) and  not pr.is_key_down(rb.KEY_M):
        print("Right")
    if pr.is_key_down(rb.KEY_PERIOD) and pr.is_key_down(rb.KEY_COMMA):
        print("Strafe Left")
    if pr.is_key_down(rb.KEY_PERIOD) and (pr.is_key_down(rb.KEY_LEFT_SHIFT) or pr.is_key_down(rb.KEY_RIGHT_SHIFT)):
        print("Strafe Right")
    pr.end_drawing()
pr.close_window()
