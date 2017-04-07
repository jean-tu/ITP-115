from Weapon import Weapon
from Melee import Melee
from Ranged import Ranged
from ZoomRanged import ZoomRanged

def main():

#   # when only Weapon has been created
    # w = Weapon(100, "generic weapon")
    # print(w)

#   # The steps after the Weapon and Melee was created
    # w = Weapon(100, "generic weapon")
    # m = Melee(10, "excalibur", 70)
    # print(w)
    # m.use()
    # print(m)

#   #when Weapon, Melee, and Ranged are created
#     w = Weapon(100, "Generic Weapon")
#     m = Melee(10, "Excalibur", 70)
#     r = Ranged(20, "Light Stick", 6)
#     r.use()
#     r.use()
#     r.use()
#     print(r)

    #when Weapon, Melee, Ranged,  and ZoomRanged are created
    w = Weapon(100, "Generic Weapon")
    m = Melee(10, "Excalibur", 70)
    r = Ranged(20, "Light Stick", 6)
    z = ZoomRanged(20, "Light Stick", 30)
    z.use()
    z.use()
    z.use()

    armory = [w,m,r,z]
    for weapon in armory:
        weapon.use()
        print(weapon)

main()