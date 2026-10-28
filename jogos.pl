jogo(the_sims_4, simulacao, single_player, pc).
jogo(minecraft, simulacao, multiplayer, pc).
jogo(stardew_valley, rpg, single_player, pc).
jogo(hollow_knight, metroidvania, single_player, pc).
jogo(portal_2, puzzle, multiplayer, pc).
jogo(hades, roguelike, single_player, nintendo_switch).
jogo(it_takes_two, aventura, multiplayer, playstation).

recomendar(Genero, Modo, Plataforma, Jogo) :-
    jogo(Jogo, Genero, Modo, Plataforma).