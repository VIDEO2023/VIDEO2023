{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOa1ryHb1wlte8A4YP5yoPA",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/VIDEO2023/VIDEO2023/blob/main/proyect.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "#declarar el arreglo\n",
        "\n",
        "arreglo=np.array([[10,20,30],\n",
        "                 [40,50,60],\n",
        "                 [70,80,90]])\n",
        "totalFilas=len(arreglo)\n",
        "\n",
        "totalColumnas=len(arreglo[0])\n",
        "\n",
        "print(\"el total de las filas es:\",totalFilas)\n",
        "print(\"el total de las columnas es:\",totalColumnas)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hNYw0-DSbIyi",
        "outputId": "78befc42-238a-417a-bd43-41c0d66d7e6f"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "el total de las filas es: 3\n",
            "el total de las columnas es: 3\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "D_9vIfRIa2nF"
      },
      "outputs": [],
      "source": [
        "import numpy as np\n",
        "\n",
        "arreglo=np.array([30,2100,30,2.4])\n",
        "\n",
        "numeroMaximo=max(arreglo)\n",
        "print(f\"el numero maximo es :{numeroMaximo}\")\n",
        "\n"
      ]
    }
  ]
}