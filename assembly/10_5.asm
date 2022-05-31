assume cs:codesg

stack segment
	dw 8 dup (0)
stack ends

codesg segment

	start:	mov ax, stack
			mov s, ax
			mov sp, 16
			mov ds, ax
			mov ax, 0
			
			call word ptr ds:[0EH]

			inc ax
			inc ax
			inc ax

			mov ax, 4c00H
			int 21h

codesg ends

end start

