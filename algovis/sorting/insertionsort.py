"""
Author: Mayank Arora (hotshot07)
"""
from ._base_class import BaseClass
from ._timer import Timer
from ._animation import AnimateAlgorithm
import copy


class InsertionSort(BaseClass):

    def __init__(self, datalist):
        super().__init__(datalist)
        self.__datalist = datalist

    def __repr__(self):
        return f'algovis.sorting.insertionsort.InsertionSort({self.__datalist})'

    # A generator for the ascending insertion sort algorithm
    # self is passed and it yields list after every iteration
    # till the list is sorted

    def __ascending_sort_algo(self):
        asc_list = copy.deepcopy(self.__datalist)
        length_of_list = len(asc_list)

        for i in range(1, length_of_list):

            key = asc_list[i]
            j = i - 1

            while j >= 0 and key < asc_list[j]:
                asc_list[j + 1] = asc_list[j]
                j -= 1

            asc_list[j + 1] = _key

            yield asc_list

    # A generator for the descending insertion sort algorithm
    # works in same way as the ascending sort algorithm

    def __descending_sort_algo(self):
        desc_list = copy.deepcopy(self.__datalist)
        length_of_list = len(desc_list)

        for i in range(1, length_of_list):

            key = desc_list[i]
            j = i - 1

            while j >= 0 and key > desc_list[j]:
                desc_list[j + 1] = desc_list[j]
                j -= 1

            desc_list[j + 1] = key

            yield desc_list

    # The function that is called by sort method
    # It checks which generator to call and if we have to show steps
    # It stores every iteration of yielded list in a dictionary
    # If steps is true, then _print_steps is called from BaseClass
    # and the dictionary iteration_dict is passed to it
    # function returns iteration_dict

    def __sort_it(self, reverse, steps):
        iteration_dict = {}
        iterations = 0

        # the 0th iteration is basically the passed list
        iteration_dict[iterations] = self.__datalist

        if not reverse:
            for yielded_list in self.__ascending_sort_algo():
                iterations += 1
                iteration_dict[iterations] = copy.deepcopy(yielded_list)
        else:
            for yielded_list in self.__descending_sort_algo():
                iterations += 1
                iteration_dict[iterations] = copy.deepcopy(yielded_list)

        if steps:
            super()._print_steps(iteration_dict)

        return iteration_dict

    # Evaluating time of ascending bubble sort
    # Didn't use generators as I dont want to waste time in
    # function overheads
    # returns a list of time taken to sort the list
    # the number of emelemts in the list will be equal to number of iterations
    # default number of iterations is 1

    def __time_eval_asc(self, iterations):
        time_list = copy.deepcopy(self.__datalist)
        length_of_list = len(time_list)
        timing_list = []

        while iterations:
            timer = Timer()
            timer.start()

            for i in range(1, length_of_list):

                key = time_list[i]
                j = i - 1

                while j >= 0 and key < time_list[j]:
                    time_list[j + 1] = time_list[j]
                    j -= 1

                time_list[j + 1] = key

            stop = timer.stop()
            timing_list.append(stop)
            iterations -= 1
            time_list = copy.deepcopy(self.__datalist)

        return timing_list

    # Evaluating time of descending insertion sort
    # works in same way as __time_eval_asc method

    def __time_eval_desc(self, iterations):
        time_list = copy.deepcopy(self.__datalist)
        length_of_list = len(time_list)
        timing_list = []

        while iterations:
            timer = Timer()
            timer.start()

            for i in range(1, length_of_list):

                key = time_list[i]
                j = i - 1

                while j >= 0 and key > time_list[j]:
                    time_list[j + 1] = time_list[j]
                    j -= 1

                time_list[j + 1] = key

            stop = timer.stop()
            timing_list.append(stop)
            iterations -= 1
            time_list = copy.deepcopy(self.__datalist)

        return timing_list

    # Sort method
    # Takes in 2 arguments reverse and steps
    # if reverse is true, it sorts it in reverse order
    # if steps is true, it shows the steps of every iteration
    # it returns the last element in the dictionary, which
    # is the sorted list

    def sort(self, reverse=False, steps=False):
        _sorted_object = self.__sort_it(reverse, steps)
        return list(_sorted_object.values())[-1]

    # Evauate method
    # Takes in 2 arguments reverse and iterations
    # if reverse is true, it sorts it in reverse order
    # default of iterations is 1
    # default of reverse is false
    # it uses the __time_eval_asc or __time_eval_desc
    # accordingly and gets a _timing list consisting
    # of time(in nanosecond) it took to sort the list
    # the dictionary _eval_dict is passed to _print_evaluate
    # present in BaseClass to print it

    def evaluate(self, reverse=False, iterations=1):
        if reverse:
            _timing_list = self.__time_eval_desc(iterations)
        else:
            _timing_list = self.__time_eval_asc(iterations)

        _minimum_time = min(_timing_list)
        _maximum_time = max(_timing_list)
        _average_time = int(sum(_timing_list) / iterations)

        _eval_dict = {
            "Minimum Time": _minimum_time,
            "Maximum Time": _maximum_time,
            "Average Time": _average_time
        }

        return super()._print_evaluate(eval_dict)

    # visualize method to visualise the sorting happeneing
    # Takes in 2 arguments reverse and interval
    # AnimateAlgorithm from _animation is used to generate figures
    # if reverse is true, AnimateAlgorithm calls the  __descending_sort_algo() generator
    # interval is used to set the speed of visualization, 250 is default.

    def visualize(self, reverse=False, interval=250):
        _vis_list = copy.deepcopy(self.__datalist)

        if not reverse:
            AnimateAlgorithm("Insertion Sort", _vis_list, self.__ascending_sort_algo(), interval)
        else:
            AnimateAlgorithm("Insertion Sort", _vis_list, self.__descending_sort_algo(), interval)

    # info class method
    # path to the markdown file is passed here
    # and _print_info from BaseClass is used to render it

    @classmethod
    def info(cls):
        path_to_information = "algovis/sorting/_markdown_files/insertionsort.md"
        return super()._print_info(path_to_information)