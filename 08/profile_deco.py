import cProfile
import io
import pstats

profile_dict = {}


def profile_deco(func):
    global profile_dict

    def wrapper(*args, **kwargs):
        func_name = func.__name__
        if func_name not in profile_dict:
            profile_dict[func_name] = cProfile.Profile()

        profile_dict[func_name].runcall(func, *args, **kwargs)

    def print_stat():
        func_name = func.__name__
        if func_name in profile_dict:
            s = io.StringIO()
            sort_by = "cumulative"
            ps = pstats.Stats(
                profile_dict[func_name], stream=s
            ).sort_stats(sort_by)
            ps.print_stats()
            print(s.getvalue())

    wrapper.print_stat = print_stat
    if func.__name__ in profile_dict:
        wrapper.kkk = print_stat

    return wrapper
