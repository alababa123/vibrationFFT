import requests
import matplotlib.pyplot as plt

def get_data_from_server():
    url = 'http://localhost:2000/api/data/get/'  # Замените на ваш URL
    response = requests.post(url, json={
        'from': 0,
        'to': 10000
    })

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return None

def plot_graph(data):
    print(data)

    # if data:
    #     time = [int(entry['time']) for entry in data]
    #     acceleration = [entry['acceleration'] for entry in data]

    #     plt.plot(time, acceleration)
    #     plt.title('Acceleration over Time')
    #     plt.xlabel('Time')
    #     plt.ylabel('Acceleration')
    #     plt.show()
    # else:
    #     print("No data to plot.")

if __name__ == "__main__":
    data_from_server = get_data_from_server()
    plot_graph(data_from_server)
