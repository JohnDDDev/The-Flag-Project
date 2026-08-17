# import pygame
# import time
#
# import main
# from Database import load_game,save_game
# import sys
#
#
# def fild_game() :
#     pygame.init()
#
#     keys_timer={}
#     current_game_state= main.current_game
#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             elif event.type == pygame.KEYDOWN:
#                 if pygame.K_1 <= event.key <= pygame.K_9:
#                     slot = event.key - pygame.K_0
#                     keys_timer[event.key] = time.time()
#
#
#             elif event.key == pygame.KEYUP:
#                 if pygame.K_1 <= event.key <= pygame.K_9:
#                     slot_num = event.key - pygame.K_0
#
#                     if event.key in keys_timer:
#                         press_time=(time.time() - keys_timer[event.key])
#                         del keys_timer[event.key]
#
#                         if press_time<=1.0:
#                             print(f"short press {press_time}")
#                             save_game(slot_num,current_game_state)
#
#                         else:
#                             print(f"long press {press_time}")
#                             load_data=load_game(slot_num)
#                             if load_data:
#                                 print(f"data to aply :{load_data}")
#         pygame.display.flip()
#     pygame.quit()
#     sys.exit()