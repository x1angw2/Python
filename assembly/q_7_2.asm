; 用 si 和 di 实现将字符串“welcome to masm!” 复制到它后面的数据中
assume cs:codesg, ds:datasg

datasg segment
	db 'welcome to masm!'
	db 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
datasg ends

codesg segment

	start:	mov ax,datasg
			mov ds,ax
			
			mov cx,8
			mov si,0
			;mov di,0
			mov di,10h
			;mov [di],[si]
		s:	mov ax, [si]
			;mov [10h + di],ax
			mov [di],ax
			add si,2
			add di,2

			loop s

			mov ax, 4c00h
			int 21h

codesg ends

end start

