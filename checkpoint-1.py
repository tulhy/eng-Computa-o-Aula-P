#NOTAS DE 0 A 5
cp1 = float(input("chekpoint 1 (0 a 10): "))
cp2 = float(input("chekpoint 2 (0 a 10): "))
cp3 = float(input("chekpoint 3 (0 a 10): "))
sp1 = float(input("sprint 1 (0 a 10): "))
sp2 = float(input("sprint 2 (0 a 10): "))
gs = float(input("Global solution (0 a 10): "))

checkpoints = [cp1, cp2, cp3]

if cp1 <= cp2 and cp1 <= cp3:
        cp_media1 = cp2
        cp_media2 = cp3
elif cp2 <= cp1 and cp2 <= cp3:
        cp_media1 = cp1
        cp_media2 = cp3
else:
        cp_media1 = cp1
        cp_media2 = cp2

media_40 = (cp_media1 + cp_media2 + sp1 + sp2)

media_final = (media_40 * 0.4) + (gs * 0.6)
if media_final >= 10:
    media_final = 10

print(f"Media semestral = {media_final:.1f}")