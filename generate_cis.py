import matplotlib.pyplot as plt
import sys

def draw_cistercian_number(num: int, output_file: str):
    if num > 9999 or num < 1:
        print("Number out of range (1 to 9999)")
        return

    numbers = [
        [  # ones
            [[50,10],[70,10]],
            [[50,30],[70,30]],
            [[50,10],[70,30]],
            [[50,30],[70,10]],
            [[50,10],[70,10],[50,30]],
            [[70,10],[70,30]],
            [[50,10],[70,10],[70,30]],
            [[50,30],[70,30],[70,10]],
            [[50,10],[70,10],[70,30],[50,30]]
        ],
        [  # tens
            [[50,10],[30,10]],
            [[50,30],[30,30]],
            [[50,10],[30,30]],
            [[50,30],[30,10]],
            [[50,10],[30,10],[50,30]],
            [[30,10],[30,30]],
            [[50,10],[30,10],[30,30]],
            [[50,30],[30,30],[30,10]],
            [[50,10],[30,10],[30,30],[50,30]]
        ],
        [  # hundreds
            [[50,90],[70,90]],
            [[50,70],[70,70]],
            [[50,90],[70,70]],
            [[50,70],[70,90]],
            [[50,90],[70,90],[50,70]],
            [[70,90],[70,70]],
            [[50,90],[70,90],[70,70]],
            [[50,70],[70,70],[70,90]],
            [[50,90],[70,90],[70,70],[50,70]]
        ],
        [  # thousands
            [[50,90],[30,90]],
            [[50,70],[30,70]],
            [[50,90],[30,70]],
            [[50,70],[30,90]],
            [[50,90],[30,90],[50,70]],
            [[30,90],[30,70]],
            [[50,90],[30,90],[30,70]],
            [[50,70],[30,70],[30,90]],
            [[50,90],[30,90],[30,70],[50,70]]
        ]
    ]

    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    plt.axis('off')

    ax.plot([50, 50], [10, 90], color='black', linewidth=1.5)

    string_num = str(num).zfill(4)

    for i in range(4):
        digit = int(string_num[3 - i])
        if digit == 0:
            continue

        coords = numbers[i][digit - 1]
        x, y = zip(*coords)
        ax.plot(x, y, color='black', linewidth=1.5)

    plt.xlim(10, 90)
    plt.ylim(0, 100)
    ax.invert_yaxis()
    plt.savefig(output_file, bbox_inches='tight', pad_inches=0.1)
    plt.close()
    print(f"Cistercian number saved to '{output_file}'")

if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python draw_cistercian.py <number> [output_file.png]")
    else:
        try:
            num = int(sys.argv[1])
            filename = sys.argv[2] if len(sys.argv) == 3 else f"cistercian_{num}.png"
            draw_cistercian_number(num, filename)
        except ValueError:
            print("Please provide a valid integer.")