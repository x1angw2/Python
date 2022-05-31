assume cs:codesg

codesg segment

	start:	mov ax,2000h
			mov es,ax
			jmp dword ptr es:[1000h]

codesg ends

end start

