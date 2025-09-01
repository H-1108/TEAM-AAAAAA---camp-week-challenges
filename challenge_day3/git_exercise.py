from kaixin import get_kaixin
from gengxin import get_gengxin
from liangyu1 import get_liangyu
from maggie import get_maggie
from tongfei import get_tongfei
from yangyang import get_yangyang

def team_name():
    return "This is Team AAAAAA. We are:", get_kaixin(), get_gengxin(), get_liangyu(), get_maggie(), get_tongfei(), get_yangyang()
    


if __name__ == "__main__":
    print(team_name())

