##
## EPITECH PROJECT, 2021
## 305construction
## File description:
## Makefile
##

MAIN		=		reedpipes.py

NAME	=		308reedpipes

all:	$(NAME)

$(NAME):
		cp $(MAIN) $(NAME)
		chmod 755 $(NAME)

clean:

fclean:	clean
		rm -rf $(NAME)

re:	fclean all