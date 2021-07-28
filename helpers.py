def create_text(window_surface, x, y, phrase, font,
                fore_color, back_color=(), align_x="left", align_y="top", get_surf=False):
    if back_color:
        text_surface_obj = font.render(phrase, True, fore_color, back_color)
    else:
        text_surface_obj = font.render(phrase, True, fore_color)
    if get_surf:
        return text_surface_obj
    text_rect_obj = text_surface_obj.get_rect()
    if align_x == "middle":
        text_rect_obj.centerx = x
    elif align_x == "right":
        text_rect_obj.right = x
    else:
        text_rect_obj.left = x
    if align_y == "middle":
        text_rect_obj.centery = y
    elif align_y == "bottom":
        text_rect_obj.bottom = y
    else:
        text_rect_obj.top = y
    window_surface.blit(text_surface_obj, text_rect_obj)
