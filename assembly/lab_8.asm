assume cs:codesg

codesg segment

			mov ax, 4c00h
			int 21h

	start:	mov ax,0
		s:	nop							; 空指令  一个字节
			nop

			mov di,offset s
			mov si,offset s2
			mov ax,cs:[si]
			mov cs:[di],ax

	s0: 	jmp short s
	s1:		mov ax, 0
			int 21h
			mov ax, 0

	s2:		jmp short s1
			nop


;  虽然把 s2 的指令复制到 s 处
;  但是 s2 指向的 s1 的是相对偏移量
;  复制到 s 处的 也是 相对 s1 的偏移量
;  并不能正确的指向 s1

codesg ends

end start

