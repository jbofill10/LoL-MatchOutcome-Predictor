import seaborn as sns
import matplotlib.pyplot as plt



def visualize(model_results):

    fig, axs = plt.subplots(2,2, figsize=(12.8, 8))
    grid_counter = 0
    dict_values = list(model_results.values())
    dict_keys = list(model_results.keys())

    for i in range(2):
        for j in range(2):
            sns.heatmap(dict_values[grid_counter], cmap='Blues', cbar=False, annot=True,
                        fmt='g', annot_kws={'size': 12}, ax=axs[i][j])

            axs[i][j].title.set_text(dict_keys[grid_counter])

            grid_counter += 1
    plt.tight_layout()
    plt.savefig('Charts/matrix_subplot.png')
    plt.show()
