def main():
    matching_names = []
    name_data = {'Mick': {2010: 2, 2000: 1, 1910: 10}, 'Sam': 2021, 'Tim': 2022}
    target = 'Mick'
    y = name_data[target].get(1910)
    if y is None:
        print('**')
    else:
        x = name_data[target][1910]
        print(x)


if __name__ == "__main__":
    main()