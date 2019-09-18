{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "“dolu4031_Ass2.ipynb”的副本",
      "version": "0.3.2",
      "provenance": [],
      "collapsed_sections": [],
      "toc_visible": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ym0vUBkl-lps",
        "colab_type": "text"
      },
      "source": [
        "#Assignment 2"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "k2QbKPEI-D2T",
        "colab_type": "text"
      },
      "source": [
        "##1. Data for Assignment 2"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "TB_D8trA-IZO",
        "colab_type": "text"
      },
      "source": [
        "###1.1 Download datasets"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Ti0YrvvQ9py8",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "!pip install -U -q PyDrive\n",
        "from pydrive.auth import GoogleAuth\n",
        "from pydrive.drive import GoogleDrive\n",
        "from google.colab import auth\n",
        "from oauth2client.client import GoogleCredentials\n",
        "\n",
        "import pandas as pd\n",
        "\n",
        "\n",
        "# Authenticate and create the PyDrive client.\n",
        "auth.authenticate_user()\n",
        "gauth = GoogleAuth()\n",
        "gauth.credentials = GoogleCredentials.get_application_default()\n",
        "drive = GoogleDrive(gauth)\n",
        "\n",
        "# Download all three Microsoft BotBuilder Personality Chat Datasets on Google Colab virtual server\n",
        "\n",
        "id = '1SXoGbD9WZHwhpqR-cBw7-8_7Ri06nIb6'\n",
        "downloaded = drive.CreateFile({'id':id }) \n",
        "downloaded.GetContentFile('WikiQA-train.tsv') \n",
        "\n",
        "id = '1TwuDSxlcAFDnTRpF-GRvqRXoR_UsJznH'\n",
        "downloaded = drive.CreateFile({'id':id }) \n",
        "downloaded.GetContentFile('WikiQA-test.tsv') "
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "sgCdHVVd-6zN",
        "colab_type": "code",
        "outputId": "1f84913c-a83e-431b-bbb9-54e7d46741ef",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 289
        }
      },
      "source": [
        "# train.tsv\n",
        "df_train=pd.read_csv('WikiQA-train.tsv', sep='\\t')\n",
        "df_train.head()"
      ],
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>QuestionID</th>\n",
              "      <th>Question</th>\n",
              "      <th>DocumentID</th>\n",
              "      <th>DocumentTitle</th>\n",
              "      <th>SentenceID</th>\n",
              "      <th>Sentence</th>\n",
              "      <th>Label</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Q1</td>\n",
              "      <td>how are glacier caves formed?</td>\n",
              "      <td>D1</td>\n",
              "      <td>Glacier cave</td>\n",
              "      <td>D1-0</td>\n",
              "      <td>A partly submerged glacier cave on Perito More...</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Q1</td>\n",
              "      <td>how are glacier caves formed?</td>\n",
              "      <td>D1</td>\n",
              "      <td>Glacier cave</td>\n",
              "      <td>D1-1</td>\n",
              "      <td>The ice facade is approximately 60 m high</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>Q1</td>\n",
              "      <td>how are glacier caves formed?</td>\n",
              "      <td>D1</td>\n",
              "      <td>Glacier cave</td>\n",
              "      <td>D1-2</td>\n",
              "      <td>Ice formations in the Titlis glacier cave</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>Q1</td>\n",
              "      <td>how are glacier caves formed?</td>\n",
              "      <td>D1</td>\n",
              "      <td>Glacier cave</td>\n",
              "      <td>D1-3</td>\n",
              "      <td>A glacier cave is a cave formed within the ice...</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>Q1</td>\n",
              "      <td>how are glacier caves formed?</td>\n",
              "      <td>D1</td>\n",
              "      <td>Glacier cave</td>\n",
              "      <td>D1-4</td>\n",
              "      <td>Glacier caves are often called ice caves , but...</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "  QuestionID  ... Label\n",
              "0         Q1  ...     0\n",
              "1         Q1  ...     0\n",
              "2         Q1  ...     0\n",
              "3         Q1  ...     1\n",
              "4         Q1  ...     0\n",
              "\n",
              "[5 rows x 7 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 3
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "OymUX5sM-7WX",
        "colab_type": "code",
        "outputId": "87d4e06d-13b1-45aa-f63b-c7f0c58df56e",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 340
        }
      },
      "source": [
        "# test.tsv\n",
        "df_test=pd.read_csv('WikiQA-test.tsv', sep='\\t')\n",
        "df_test.head()"
      ],
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>QuestionID</th>\n",
              "      <th>Question</th>\n",
              "      <th>DocumentID</th>\n",
              "      <th>DocumentTitle</th>\n",
              "      <th>SentenceID</th>\n",
              "      <th>Sentence</th>\n",
              "      <th>Label</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Q0</td>\n",
              "      <td>HOW AFRICAN AMERICANS WERE IMMIGRATED TO THE US</td>\n",
              "      <td>D0</td>\n",
              "      <td>African immigration to the United States</td>\n",
              "      <td>D0-0</td>\n",
              "      <td>African immigration to the United States refer...</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Q0</td>\n",
              "      <td>HOW AFRICAN AMERICANS WERE IMMIGRATED TO THE US</td>\n",
              "      <td>D0</td>\n",
              "      <td>African immigration to the United States</td>\n",
              "      <td>D0-1</td>\n",
              "      <td>The term African in the scope of this article ...</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>Q0</td>\n",
              "      <td>HOW AFRICAN AMERICANS WERE IMMIGRATED TO THE US</td>\n",
              "      <td>D0</td>\n",
              "      <td>African immigration to the United States</td>\n",
              "      <td>D0-2</td>\n",
              "      <td>From the Immigration and Nationality Act of 19...</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>Q0</td>\n",
              "      <td>HOW AFRICAN AMERICANS WERE IMMIGRATED TO THE US</td>\n",
              "      <td>D0</td>\n",
              "      <td>African immigration to the United States</td>\n",
              "      <td>D0-3</td>\n",
              "      <td>African immigrants in the United States come f...</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>Q0</td>\n",
              "      <td>HOW AFRICAN AMERICANS WERE IMMIGRATED TO THE US</td>\n",
              "      <td>D0</td>\n",
              "      <td>African immigration to the United States</td>\n",
              "      <td>D0-4</td>\n",
              "      <td>They include people from different national, l...</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "  QuestionID  ... Label\n",
              "0         Q0  ...     0\n",
              "1         Q0  ...     0\n",
              "2         Q0  ...     0\n",
              "3         Q0  ...     0\n",
              "4         Q0  ...     0\n",
              "\n",
              "[5 rows x 7 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 3
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "cJFAv5Rq-dTE",
        "colab_type": "text"
      },
      "source": [
        "###1.2 Data Wrangling"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "R_SNMu7z_0WT",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "import spacy\n",
        "nlp = spacy.load(\"en_core_web_sm\")\n",
        "\n",
        "def data_wrangling(df):\n",
        "  Q = {}\n",
        "  D = {}\n",
        "  Dpos = {}\n",
        "  Ddep = {}\n",
        "  Dent = {}\n",
        "  A = {}\n",
        "#   Apos = {}\n",
        "#   Adep = {}\n",
        "#   Aent = {}\n",
        "\n",
        "  for index, row in df.iterrows():\n",
        "    if row['QuestionID'] not in Q:\n",
        "      Q[row['QuestionID']] = []\n",
        "      token1 = nlp(row['Question'])\n",
        "      for i in token1:\n",
        "        Q[row['QuestionID']].append(i.text.lower())\n",
        "      Q[row['QuestionID']].append(row['DocumentID'])\n",
        "    if row['DocumentID'] not in D:\n",
        "      token2 = nlp(row['Sentence'])\n",
        "      D[row['DocumentID']] = []\n",
        "      Dpos[row['DocumentID']] = []\n",
        "      Ddep[row['DocumentID']] = []\n",
        "      Dent[row['DocumentID']] = []\n",
        "      temp = []\n",
        "      temppos = []\n",
        "      tempdep = []\n",
        "      tempent = []\n",
        "      for i in token2:\n",
        "        #get document token as well as its PoS tag, Dependency Path, and Named Entity tag\n",
        "        temp.append(i.text.lower())\n",
        "        temppos.append(i.pos_)\n",
        "        tempdep.append(i.dep_)\n",
        "        tempent.append(i.ent_type_)\n",
        "      D[row['DocumentID']].append(temp)\n",
        "      Dpos[row['DocumentID']].append(temppos)\n",
        "      Ddep[row['DocumentID']].append(tempdep)\n",
        "      Dent[row['DocumentID']].append(tempent)\n",
        "    else:\n",
        "      token2 = nlp(row['Sentence'])\n",
        "      temp = []\n",
        "      temppos = []\n",
        "      tempdep = []\n",
        "      tempent = []\n",
        "      for i in token2:\n",
        "        temp.append(i.text.lower())\n",
        "        temppos.append(i.pos_)\n",
        "        tempdep.append(i.dep_)\n",
        "        tempent.append(i.ent_type_)\n",
        "      D[row['DocumentID']].append(temp)\n",
        "      Dpos[row['DocumentID']].append(temppos)\n",
        "      Ddep[row['DocumentID']].append(tempdep)\n",
        "      Dent[row['DocumentID']].append(tempent)\n",
        "    if row['QuestionID'] not in A:\n",
        "      A[row['QuestionID']] = []\n",
        "      A[row['QuestionID']].append(row['Label'])\n",
        "    else:\n",
        "      A[row['QuestionID']].append(row['Label'])\n",
        "        \n",
        "  dataset = integrate_doc_data(Q, D, A)\n",
        "  pos = integrate_feature_data(Q, Dpos)\n",
        "  dep = integrate_feature_data(Q, Ddep)\n",
        "  ent = integrate_feature_data(Q, Dent)\n",
        "    \n",
        "  return dataset, pos, dep, ent\n",
        "\n",
        "    \n",
        "def integrate_doc_data(Q, D, A)  :\n",
        "  integrate_set = []\n",
        "  for key, value in Q.items():\n",
        "    data = {}\n",
        "    data[\"document\"] = D[value[-1]]\n",
        "    data[\"question\"] = value[: -1]\n",
        "    data[\"answer\"] = A[key]\n",
        "    \n",
        "    integrate_set.append(data)\n",
        "  return integrate_set\n",
        "\n",
        "def integrate_feature_data(Q, D)  :\n",
        "  integrate_set = []\n",
        "  for key, value in Q.items():\n",
        "    data = {}\n",
        "    data[\"document\"] = D[value[-1]]    \n",
        "    integrate_set.append(data)\n",
        "  return integrate_set"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "qX9FCrcpNTut",
        "colab_type": "code",
        "outputId": "ab7c88ce-59d6-47cc-9d3d-668dcbd61bf9",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 105
        }
      },
      "source": [
        "train_dataset, train_pos, train_dep, train_ent= data_wrangling(df_train)\n",
        "print(train_dataset[0])\n",
        "print(train_pos[0])\n",
        "print(train_dep[0])\n",
        "print(train_ent[0])"
      ],
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "{'document': [['a', 'partly', 'submerged', 'glacier', 'cave', 'on', 'perito', 'moreno', 'glacier', '.'], ['the', 'ice', 'facade', 'is', 'approximately', '60', 'm', 'high'], ['ice', 'formations', 'in', 'the', 'titlis', 'glacier', 'cave'], ['a', 'glacier', 'cave', 'is', 'a', 'cave', 'formed', 'within', 'the', 'ice', 'of', 'a', 'glacier', '.'], ['glacier', 'caves', 'are', 'often', 'called', 'ice', 'caves', ',', 'but', 'this', 'term', 'is', 'properly', 'used', 'to', 'describe', 'bedrock', 'caves', 'that', 'contain', 'year', '-', 'round', 'ice', '.']], 'question': ['how', 'are', 'glacier', 'caves', 'formed', '?'], 'answer': [0, 0, 0, 1, 0]}\n",
            "{'document': [['DET', 'ADV', 'VERB', 'NOUN', 'NOUN', 'ADP', 'PROPN', 'PROPN', 'PROPN', 'PUNCT'], ['DET', 'NOUN', 'NOUN', 'VERB', 'ADV', 'NUM', 'NOUN', 'ADJ'], ['NOUN', 'NOUN', 'ADP', 'DET', 'PROPN', 'NOUN', 'NOUN'], ['DET', 'NOUN', 'NOUN', 'VERB', 'DET', 'NOUN', 'VERB', 'ADP', 'DET', 'NOUN', 'ADP', 'DET', 'NOUN', 'PUNCT'], ['NOUN', 'NOUN', 'VERB', 'ADV', 'VERB', 'NOUN', 'NOUN', 'PUNCT', 'CCONJ', 'DET', 'NOUN', 'VERB', 'ADV', 'VERB', 'PART', 'VERB', 'NOUN', 'NOUN', 'ADJ', 'VERB', 'NOUN', 'PUNCT', 'NOUN', 'NOUN', 'PUNCT']]}\n",
            "{'document': [['det', 'advmod', 'amod', 'compound', 'ROOT', 'prep', 'compound', 'compound', 'pobj', 'punct'], ['det', 'compound', 'nsubj', 'ROOT', 'advmod', 'nummod', 'npadvmod', 'acomp'], ['compound', 'ROOT', 'prep', 'det', 'compound', 'compound', 'pobj'], ['det', 'compound', 'nsubj', 'ROOT', 'det', 'attr', 'acl', 'prep', 'det', 'pobj', 'prep', 'det', 'pobj', 'punct'], ['compound', 'nsubjpass', 'auxpass', 'advmod', 'ROOT', 'compound', 'oprd', 'punct', 'cc', 'det', 'nsubjpass', 'auxpass', 'advmod', 'conj', 'aux', 'xcomp', 'compound', 'dobj', 'nsubj', 'relcl', 'npadvmod', 'punct', 'amod', 'dobj', 'punct']]}\n",
            "{'document': [['', '', '', '', '', '', 'PERSON', 'PERSON', 'PERSON', ''], ['', '', '', '', 'CARDINAL', 'CARDINAL', 'CARDINAL', ''], ['', '', '', '', 'ORG', '', ''], ['', '', '', '', '', '', '', '', '', '', '', '', '', ''], ['ORG', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'DATE', 'DATE', 'DATE', '', '']]}\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "iPlcFKwO_NLF",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "#integrate the token and all its features\n",
        "train_data_list = []\n",
        "for i in range(len(train_dataset)):\n",
        "  train_data_sublist = []\n",
        "  for j in range(len(train_dataset[i]['document'])):\n",
        "    temp = []\n",
        "    for l in range(len(train_dataset[i]['document'][j])):\n",
        "      temp.append([train_dataset[i]['document'][j][l], train_pos[i]['document'][j][l], train_dep[i]['document'][j][l], train_ent[i]['document'][j][l]])\n",
        "      if train_dataset[i]['document'][j][l] in train_dataset[i]['question']:\n",
        "        temp[l].append(1)\n",
        "      else:\n",
        "        temp[l].append(0)\n",
        "    train_data_sublist.append(temp)\n",
        "  train_data_list.append(train_data_sublist)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "3bUnGBQrZy8K",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "#make all the question tokens into one list\n",
        "train_question_list = []\n",
        "for i in train_dataset:\n",
        "  train_question_sublist = []\n",
        "  for j in i['question']:\n",
        "    train_question_sublist.append(j)\n",
        "  train_question_list.append(train_question_sublist)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "EaAEeaQk0bl-",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "#generate a Label list of answers\n",
        "train_answer_list = []\n",
        "for i in train_dataset:\n",
        "  train_answer_list.append(i['answer'])"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "qsFzIKJhNlnN",
        "colab_type": "code",
        "outputId": "831859ed-020c-43ff-fd85-a88945a864b9",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 105
        }
      },
      "source": [
        "test_dataset, test_pos, test_dep, test_ent = data_wrangling(df_test)\n",
        "print(test_dataset[0])\n",
        "print(test_pos[0])\n",
        "print(test_dep[0])\n",
        "print(test_ent[0])"
      ],
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "{'document': [['african', 'immigration', 'to', 'the', 'united', 'states', 'refers', 'to', 'immigrants', 'to', 'the', 'united', 'states', 'who', 'are', 'or', 'were', 'nationals', 'of', 'africa', '.'], ['the', 'term', 'african', 'in', 'the', 'scope', 'of', 'this', 'article', 'refers', 'to', 'geographical', 'or', 'national', 'origins', 'rather', 'than', 'racial', 'affiliation', '.'], ['from', 'the', 'immigration', 'and', 'nationality', 'act', 'of', '1965', 'to', '2007', ',', 'an', 'estimated', 'total', 'of', '0.8', 'to', '0.9', 'million', 'africans', 'immigrated', 'to', 'the', 'united', 'states', ',', 'accounting', 'for', 'roughly', '3.3', '%', 'of', 'total', 'immigration', 'to', 'the', 'united', 'states', 'during', 'this', 'period', '.'], ['african', 'immigrants', 'in', 'the', 'united', 'states', 'come', 'from', 'almost', 'all', 'regions', 'in', 'africa', 'and', 'do', 'not', 'constitute', 'a', 'homogeneous', 'group', '.'], ['they', 'include', 'people', 'from', 'different', 'national', ',', 'linguistic', ',', 'ethnic', ',', 'racial', ',', 'cultural', 'and', 'social', 'backgrounds', '.'], ['as', 'such', ',', 'african', 'immigrants', 'are', 'to', 'be', 'distinguished', 'from', 'african', 'american', 'people', ',', 'the', 'latter', 'of', 'whom', 'are', 'descendants', 'of', 'mostly', 'west', 'and', 'central', 'africans', 'who', 'were', 'involuntarily', 'brought', 'to', 'the', 'united', 'states', 'by', 'means', 'of', 'the', 'historic', 'atlantic', 'slave', 'trade', '.']], 'question': ['how', 'african', 'americans', 'were', 'immigrated', 'to', 'the', 'us'], 'answer': [0, 0, 0, 0, 0, 1]}\n",
            "{'document': [['ADJ', 'NOUN', 'ADP', 'DET', 'PROPN', 'PROPN', 'VERB', 'ADP', 'NOUN', 'ADP', 'DET', 'PROPN', 'PROPN', 'NOUN', 'VERB', 'CCONJ', 'VERB', 'NOUN', 'ADP', 'PROPN', 'PUNCT'], ['DET', 'NOUN', 'ADJ', 'ADP', 'DET', 'NOUN', 'ADP', 'DET', 'NOUN', 'VERB', 'ADP', 'ADJ', 'CCONJ', 'ADJ', 'NOUN', 'ADV', 'ADP', 'ADJ', 'NOUN', 'PUNCT'], ['ADP', 'DET', 'PROPN', 'CCONJ', 'PROPN', 'PROPN', 'ADP', 'NUM', 'ADP', 'NUM', 'PUNCT', 'DET', 'VERB', 'NOUN', 'ADP', 'NUM', 'ADP', 'NUM', 'NUM', 'PROPN', 'VERB', 'ADP', 'DET', 'PROPN', 'PROPN', 'PUNCT', 'VERB', 'ADP', 'ADV', 'NUM', 'NOUN', 'ADP', 'ADJ', 'NOUN', 'ADP', 'DET', 'PROPN', 'PROPN', 'ADP', 'DET', 'NOUN', 'PUNCT'], ['ADJ', 'NOUN', 'ADP', 'DET', 'PROPN', 'PROPN', 'VERB', 'ADP', 'ADV', 'DET', 'NOUN', 'ADP', 'PROPN', 'CCONJ', 'VERB', 'ADV', 'VERB', 'DET', 'ADJ', 'NOUN', 'PUNCT'], ['PRON', 'VERB', 'NOUN', 'ADP', 'ADJ', 'ADJ', 'PUNCT', 'ADJ', 'PUNCT', 'ADJ', 'PUNCT', 'ADJ', 'PUNCT', 'ADJ', 'CCONJ', 'ADJ', 'NOUN', 'PUNCT'], ['ADP', 'ADJ', 'PUNCT', 'ADJ', 'NOUN', 'VERB', 'PART', 'VERB', 'VERB', 'ADP', 'ADJ', 'ADJ', 'NOUN', 'PUNCT', 'DET', 'ADJ', 'ADP', 'NOUN', 'VERB', 'NOUN', 'ADP', 'ADV', 'PROPN', 'CCONJ', 'PROPN', 'PROPN', 'NOUN', 'VERB', 'ADV', 'VERB', 'ADP', 'DET', 'PROPN', 'PROPN', 'ADP', 'NOUN', 'ADP', 'DET', 'ADJ', 'PROPN', 'NOUN', 'NOUN', 'PUNCT']]}\n",
            "{'document': [['amod', 'nsubj', 'prep', 'det', 'compound', 'pobj', 'ROOT', 'prep', 'pobj', 'prep', 'det', 'compound', 'pobj', 'nsubj', 'relcl', 'cc', 'conj', 'attr', 'prep', 'pobj', 'punct'], ['det', 'nsubj', 'appos', 'prep', 'det', 'pobj', 'prep', 'det', 'pobj', 'ROOT', 'prep', 'amod', 'cc', 'conj', 'pobj', 'advmod', 'prep', 'amod', 'pobj', 'punct'], ['prep', 'det', 'nmod', 'cc', 'conj', 'pobj', 'prep', 'pobj', 'prep', 'pobj', 'punct', 'det', 'amod', 'nsubj', 'prep', 'quantmod', 'quantmod', 'compound', 'nummod', 'pobj', 'ROOT', 'prep', 'det', 'compound', 'pobj', 'punct', 'advcl', 'prep', 'advmod', 'nummod', 'pobj', 'prep', 'amod', 'pobj', 'prep', 'det', 'compound', 'pobj', 'prep', 'det', 'pobj', 'punct'], ['amod', 'nsubj', 'prep', 'det', 'compound', 'pobj', 'ROOT', 'prep', 'advmod', 'nummod', 'pobj', 'prep', 'pobj', 'cc', 'aux', 'neg', 'conj', 'det', 'amod', 'dobj', 'punct'], ['nsubj', 'ROOT', 'dobj', 'prep', 'amod', 'amod', 'punct', 'amod', 'punct', 'amod', 'punct', 'conj', 'punct', 'conj', 'cc', 'conj', 'pobj', 'punct'], ['prep', 'amod', 'punct', 'amod', 'nsubj', 'ROOT', 'aux', 'auxpass', 'xcomp', 'prep', 'amod', 'amod', 'pobj', 'punct', 'det', 'nsubj', 'prep', 'pobj', 'relcl', 'attr', 'prep', 'advmod', 'pobj', 'cc', 'compound', 'conj', 'nsubjpass', 'auxpass', 'advmod', 'relcl', 'dative', 'det', 'compound', 'pobj', 'agent', 'pobj', 'prep', 'det', 'amod', 'compound', 'compound', 'pobj', 'punct']]}\n",
            "{'document': [['NORP', '', '', 'GPE', 'GPE', 'GPE', '', '', '', '', 'GPE', 'GPE', 'GPE', '', '', '', '', '', '', 'LOC', ''], ['', '', 'NORP', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], ['', 'EVENT', 'EVENT', 'EVENT', 'EVENT', 'EVENT', '', 'DATE', 'DATE', 'DATE', '', '', '', '', '', 'CARDINAL', '', 'CARDINAL', 'CARDINAL', 'NORP', '', '', 'GPE', 'GPE', 'GPE', '', '', '', 'PERCENT', 'PERCENT', 'PERCENT', '', '', '', '', 'GPE', 'GPE', 'GPE', '', '', '', ''], ['NORP', '', '', 'GPE', 'GPE', 'GPE', '', '', '', '', '', '', 'LOC', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], ['', '', '', 'NORP', '', '', '', '', '', '', 'NORP', 'NORP', '', '', '', '', '', '', '', '', '', '', 'LOC', '', 'NORP', 'NORP', '', '', '', '', '', 'GPE', 'GPE', 'GPE', '', '', '', '', '', 'LOC', '', '', '']]}\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "-DHjKPrIGC9e",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "test_data_list = []\n",
        "for i in range(len(test_dataset)):\n",
        "  test_data_sublist = []\n",
        "  for j in range(len(test_dataset[i]['document'])):\n",
        "    temp = []\n",
        "    for l in range(len(test_dataset[i]['document'][j])):\n",
        "      temp.append([test_dataset[i]['document'][j][l], test_pos[i]['document'][j][l], test_dep[i]['document'][j][l], test_ent[i]['document'][j][l]])\n",
        "      if test_dataset[i]['document'][j][l] in test_dataset[i]['question']:\n",
        "        temp[l].append(1)\n",
        "      else:\n",
        "        temp[l].append(0)\n",
        "    test_data_sublist.append(temp)\n",
        "  test_data_list.append(test_data_sublist)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Y45CXfoIGOws",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "test_question_list = []\n",
        "for i in test_dataset:\n",
        "  test_question_sublist = []\n",
        "  for j in i['question']:\n",
        "    test_question_sublist.append(j)\n",
        "  test_question_list.append(test_question_sublist)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "PN49ml0e_fMn",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "test_answer_list = []\n",
        "for i in test_dataset:\n",
        "  test_answer_list.append(i['answer'])"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Yhkt7SH66RWC",
        "colab_type": "text"
      },
      "source": [
        "##2. QA Framework Implementation"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "HOc_cKFJ6ZyN",
        "colab_type": "text"
      },
      "source": [
        "###2.1 Word Embeddings and Feature Extraction"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "sycPmkfCcnoy",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "#get unique token lists of documents and questions\n",
        "def doc_token_integration(dataset):\n",
        "  document_token = []\n",
        "  question_token = []\n",
        "  doc = []\n",
        "  for i in dataset:\n",
        "    for j in i['document']:\n",
        "      for l in j:\n",
        "        document_token.append(l)\n",
        "    for j in i['question']:\n",
        "      question_token.append(j)\n",
        "  return sorted(list(set(document_token))), sorted(list(set(question_token)))\n"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "DPvIHwSEG250",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "#get unique feature lists of document tokens\n",
        "def feature_token_integration(dataset):\n",
        "  feature_token = []\n",
        "  \n",
        "  for i in dataset:\n",
        "    for j in i['document']:\n",
        "      for l in j:\n",
        "        feature_token.append(l)\n",
        "  return sorted(list(set(feature_token)))\n"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "sMxfiq-Gnzrl",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "train_D_token, train_Q_token = doc_token_integration(train_dataset)\n",
        "train_Dpos_token = feature_token_integration(train_pos)\n",
        "train_Ddep_token = feature_token_integration(train_dep)\n",
        "train_Dent_token = feature_token_integration(train_ent)\n"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "EB9TJDSrqvtd",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "test_D_token, test_Q_token = doc_token_integration(test_dataset)\n",
        "test_Dpos_token = feature_token_integration(test_pos)\n",
        "test_Ddep_token = feature_token_integration(test_dep)\n",
        "test_Dent_token = feature_token_integration(test_ent)\n"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "nozfep9uvcYO",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "#get all the document tokens in a list and all the question tokens in another list\n",
        "train_documents = []\n",
        "train_questions = []\n",
        "for i in train_dataset:\n",
        "  train_questions.append(i['question'])\n",
        "  for j in i['document']:\n",
        "    train_documents.append(j)\n",
        "  "
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "YwHutlH17aOt",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "test_documents = []\n",
        "test_questions = []\n",
        "for i in test_dataset:  \n",
        "  test_questions.append(i['question'])\n",
        "  for j in i['document']:\n",
        "    test_documents.append(j)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "kivwKQxwzakz",
        "colab_type": "text"
      },
      "source": [
        "####2.1.1 Word Embeddings"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "SZPVk9BZ3Fte",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "#word2vec with skip-gram\n",
        "from gensim.models import Word2Vec\n",
        "wv_doc_train = Word2Vec(sentences=train_documents, size=100, window=5, min_count=5, workers=4, sg=1)\n",
        "wv_que_train = Word2Vec(sentences=train_questions, size=100, window=5, min_count=5, workers=4, sg=1)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "nfW_ecx37YP_",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "wv_doc_test = Word2Vec(sentences=test_documents, size=100, window=5, min_count=5, workers=4, sg=1)\n",
        "wv_que_test = Word2Vec(sentences=test_questions, size=100, window=5, min_count=5, workers=4, sg=1)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "zgauhQUd0IOu",
        "colab_type": "text"
      },
      "source": [
        "####2.1.2 Feature Extraction"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "QrgcjwAZ3cy9",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "#generate feature dictionary to convert feature tokens to vectors\n",
        "def feature_embeddings(feature_list):\n",
        "  feature_index = {}\n",
        "  for i in feature_list:\n",
        "    index = [0] * len(feature_list)\n",
        "    index[feature_list.index(i)] = 1\n",
        "    feature_index[i] = index\n",
        "  return feature_index"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ra2hzZwB6ycl",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "train_Dpos_index = feature_embeddings(train_Dpos_token)\n",
        "train_Ddep_index = feature_embeddings(train_Ddep_token)\n",
        "train_Dent_index = feature_embeddings(train_Dent_token)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "hEdF5UuBM9f_",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "test_Dpos_index = feature_embeddings(test_Dpos_token)\n",
        "test_Ddep_index = feature_embeddings(test_Ddep_token)\n",
        "test_Dent_index = feature_embeddings(test_Dent_token)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "os1Q218d0R-K",
        "colab_type": "text"
      },
      "source": [
        "####2.1.3 Generate Inputs"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "8ElUnE5ZBVI8",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "#generate document input\n",
        "def document_input(doc_list, model, Dpos_index = [], Ddep_index = [], Dent_index = [], Dmatch_index = False):\n",
        "  doc_input = []\n",
        "  for document in doc_list:\n",
        "    doc_subinput = []\n",
        "    #set the number of sentences in a document to be 20\n",
        "    if len(document) <= 20:\n",
        "      for sentence in document:\n",
        "        temp = []\n",
        "        #set the number of tokens in a sentence to be 40\n",
        "        if len(sentence) <= 40:\n",
        "          for i in sentence:\n",
        "            #add word vector\n",
        "            if i[0] in model.wv.vocab:\n",
        "              input_data = model.wv.word_vec(i[0]).tolist()\n",
        "            else:\n",
        "              #the size of word vector\n",
        "              input_data = [0] * 100\n",
        "            #add PoS tags\n",
        "            if Dpos_index != []:\n",
        "              pos_index = Dpos_index[i[1]]\n",
        "            else:\n",
        "              #the size of PoS tags\n",
        "              pos_index = [0] * 16\n",
        "            #add Dependency Path\n",
        "            if Ddep_index != []:\n",
        "              dep_index = Ddep_index[i[2]]\n",
        "            else:\n",
        "              #the size of Dependency Path\n",
        "              dep_index = [0] *46\n",
        "            #add Named Entity tags\n",
        "            if Dent_index != []:  \n",
        "              ent_index = Dent_index[i[3]]\n",
        "            else:\n",
        "              #the size of Named Entity tags\n",
        "              ent_index = [0] *19\n",
        "            for j in pos_index:\n",
        "              input_data.append(j)\n",
        "            for j in dep_index:\n",
        "              input_data.append(j)\n",
        "            for j in ent_index:\n",
        "              input_data.append(j)\n",
        "            #add Word match feature\n",
        "            if Dmatch_index is True:\n",
        "              input_data.append(i[4])\n",
        "            else:\n",
        "              input_data.append(0)\n",
        "            temp.append(input_data)\n",
        "          diff = 40 - len(sentence)\n",
        "          for i in range(diff):\n",
        "            temp.append([0]*len(temp[0]))\n",
        "        else:\n",
        "          sentence = sentence[:40]\n",
        "          for i in sentence:\n",
        "            if i[0] in model.wv.vocab:\n",
        "              input_data = model.wv.word_vec(i[0]).tolist()\n",
        "            else:\n",
        "              input_data = [0] * 100\n",
        "            if Dpos_index != []:\n",
        "              pos_index = Dpos_index[i[1]]\n",
        "            else:\n",
        "              pos_index = [0] * 16\n",
        "            if Ddep_index != []:\n",
        "              dep_index = Ddep_index[i[2]]\n",
        "            else:\n",
        "              dep_index = [0] *46\n",
        "            if Dent_index != []:  \n",
        "              ent_index = Dent_index[i[3]]\n",
        "            else:\n",
        "              ent_index = [0] *19\n",
        "            for j in pos_index:\n",
        "              input_data.append(j)\n",
        "            for j in dep_index:\n",
        "              input_data.append(j)\n",
        "            for j in ent_index:\n",
        "              input_data.append(j)\n",
        "            if Dmatch_index is True:\n",
        "              input_data.append(i[4])\n",
        "            else:\n",
        "              input_data.append(0)\n",
        "            temp.append(input_data)\n",
        "        doc_subinput.append(temp)\n",
        "      diff1 = 20 - len(document)\n",
        "      for l in range(diff1):\n",
        "        doc_subinput.append([[0]*len(temp[0])]*40)\n",
        "    else:\n",
        "      document = document[:20]\n",
        "      for sentence in document:\n",
        "        temp = []\n",
        "        if len(sentence) <= 40:\n",
        "          for i in sentence:\n",
        "            if i[0] in model.wv.vocab:\n",
        "              input_data = model.wv.word_vec(i[0]).tolist()\n",
        "            else:\n",
        "              input_data = [0] * 100\n",
        "            if Dpos_index != []:\n",
        "              pos_index = Dpos_index[i[1]]\n",
        "            else:\n",
        "              pos_index = [0] * 16\n",
        "            if Ddep_index != []:\n",
        "              dep_index = Ddep_index[i[2]]\n",
        "            else:\n",
        "              dep_index = [0] *46\n",
        "            if Dent_index != []:  \n",
        "              ent_index = Dent_index[i[3]]\n",
        "            else:\n",
        "              ent_index = [0] *19\n",
        "            for j in pos_index:\n",
        "              input_data.append(j)\n",
        "            for j in dep_index:\n",
        "              input_data.append(j)\n",
        "            for j in ent_index:\n",
        "              input_data.append(j)\n",
        "            if Dmatch_index is True:\n",
        "              input_data.append(i[4])\n",
        "            else:\n",
        "              input_data.append(0)\n",
        "            temp.append(input_data)\n",
        "          diff = 40 - len(sentence)\n",
        "          for i in range(diff):\n",
        "            temp.append([0]*len(temp[0]))\n",
        "        else:\n",
        "          sentence = sentence[:40]\n",
        "          for i in sentence:\n",
        "            if i[0] in model.wv.vocab:\n",
        "              input_data = model.wv.word_vec(i[0]).tolist()\n",
        "            else:\n",
        "              input_data = [0] * 100\n",
        "            if Dpos_index != []:\n",
        "              pos_index = Dpos_index[i[1]]\n",
        "            else:\n",
        "              pos_index = [0] * 16\n",
        "            if Ddep_index != []:\n",
        "              dep_index = Ddep_index[i[2]]\n",
        "            else:\n",
        "              dep_index = [0] *46\n",
        "            if Dent_index != []:  \n",
        "              ent_index = Dent_index[i[3]]\n",
        "            else:\n",
        "              ent_index = [0] *19\n",
        "            for j in pos_index:\n",
        "              input_data.append(j)\n",
        "            for j in dep_index:\n",
        "              input_data.append(j)\n",
        "            for j in ent_index:\n",
        "              input_data.append(j)\n",
        "            if Dmatch_index is True:\n",
        "              input_data.append(i[4])\n",
        "            else:\n",
        "              input_data.append(0)\n",
        "            temp.append(input_data)\n",
        "        doc_subinput.append(temp)\n",
        "      diff1 = 20 - len(document)\n",
        "      for l in range(diff1):\n",
        "        doc_subinput.append([[0]*len(temp[0])]*40)\n",
        "    doc_input.append(doc_subinput)\n",
        "  return doc_input"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "MlMHn_tlUC-G",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "#generate document input with all these four features being taken into consideration\n",
        "train_doc_input = document_input(train_data_list, wv_doc_train, Dpos_index = train_Dpos_index, Ddep_index = train_Ddep_index, Dent_index = train_Dent_index, Dmatch_index = True)\n",
        "test_doc_input = document_input(test_data_list, wv_doc_test, Dpos_index = test_Dpos_index, Ddep_index = test_Ddep_index, Dent_index = test_Dent_index, Dmatch_index = True)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "djy17UZCXVWu",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "#generate question input\n",
        "def question_input(que_list, model):\n",
        "  que_input = []\n",
        "  for question in que_list:\n",
        "    que_subinput = []\n",
        "    #set the number of tokens in a question to be 20\n",
        "    if len(question) <= 20:\n",
        "      for i in question:\n",
        "        #add word vector\n",
        "        if i in model.wv.vocab:\n",
        "          input_data = model.wv.word_vec(i).tolist()\n",
        "        else:\n",
        "          #the size of word vector\n",
        "          input_data = [0] * 100\n",
        "        que_subinput.append(input_data)\n",
        "      diff = 20 - len(question)\n",
        "      for i in range(diff):\n",
        "        que_subinput.append([0] * 100)\n",
        "    else:\n",
        "      question = question[:20]\n",
        "      for i in question:\n",
        "        if i in model.wv.vocab:\n",
        "          input_data = model.wv.word_vec(i).tolist()\n",
        "        else:\n",
        "          input_data = [0] * 100\n",
        "        que_subinput.append(input_data)\n",
        "    que_input.append(que_subinput)\n",
        "  return que_input"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "zXZCmuZ4ASOE",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "train_que_input = question_input(train_question_list, wv_que_train)\n",
        "test_que_input = question_input(test_question_list, wv_que_test)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "0ziS5Umw04y_",
        "colab_type": "text"
      },
      "source": [
        "####2.1.4 Generate Target Outputs"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "UBkbtNaR_w66",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "#generate target answer output\n",
        "def answer_sentence_output(ans_list):\n",
        "  ans_output = []\n",
        "  for i in ans_list:\n",
        "    #the number of sentences in a document is 20\n",
        "    ans_suboutput = [0] * 20\n",
        "    if len(i) <= 20:\n",
        "      for j in range(len(i)):\n",
        "        ans_suboutput[j] = i[j]\n",
        "\n",
        "    else:\n",
        "      for j in range(20):\n",
        "        ans_suboutput[j] = i[j]\n",
        "    ans_output.append(ans_suboutput)\n",
        "  return ans_output"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "GicN6C-MAWO-",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "train_answer = answer_sentence_output(train_answer_list)\n",
        "test_answer = answer_sentence_output(test_answer_list)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "6bTcyZuf1BH2",
        "colab_type": "text"
      },
      "source": [
        "###2.2 Sequence Model"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Bm5oVza5Ar2N",
        "colab_type": "code",
        "outputId": "b501e0d1-517f-4981-9bce-a3dee9006299",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 621
        }
      },
      "source": [
        "from keras.utils import plot_model\n",
        "from keras.models import Model\n",
        "from keras.layers import Input, Dense, Reshape, Bidirectional, dot, Activation\n",
        "from keras.layers.recurrent import LSTM\n",
        "from keras import backend \n",
        "from IPython.display import display, Image\n",
        "\n",
        "input1 = Input(shape=(20, 40, 182))\n",
        "reshape1 = Reshape((20, 40*182))(input1)\n",
        "extract1 = Bidirectional(LSTM(200, return_sequences=True), merge_mode='sum')(reshape1)\n",
        "\n",
        "input2 = Input(shape=(20, 100))\n",
        "extract2 = Bidirectional(LSTM(200), merge_mode='sum')(input2)\n",
        "\n",
        "merge1 = dot([extract1, extract2], axes=-1)\n",
        "\n",
        "output = Activation('sigmoid')(merge1)\n",
        "\n",
        "model = Model(inputs=[input1, input2], outputs=output)\n",
        "\n",
        "plot_model(model, to_file='Assignment2.png', show_shapes=True)\n",
        "display(Image(filename='Assignment2.png'))"
      ],
      "execution_count": 34,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Using TensorFlow backend.\n"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "WARNING:tensorflow:From /usr/local/lib/python3.6/dist-packages/tensorflow/python/framework/op_def_library.py:263: colocate_with (from tensorflow.python.framework.ops) is deprecated and will be removed in a future version.\n",
            "Instructions for updating:\n",
            "Colocations handled automatically by placer.\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\nFi6XK/mwvRhZwu3SO7nHn2SHzifSv/sNAEC5oAQFAIB+xmazq6qq5B1Fz5qamgghbDZbTB8OhxMf\nH89gMD766CPRX6hqamoIIZqamqKdtbW16+rqetwufRHp5s2bhU96fPjwIT2HjSRSUlJ2796dk5Mz\nevRo4Ur6htva2lrhGoFA0NTUZGRkJOGwvRtZwu3SlRW9w8UYOp9I/+43AADlghIUAAD6U2tra01N\njYmJibwD6Rn99z19A6oYtra2a9euvXv37vbt24UrtbW1CSGdyhsJ37i+vj4hJCoqSnSG+itXrkgS\n8/79+5OSki5evDhixAjR9WZmZjwe7+HDh8I19O21EyZMkGTYXo8s4XZbWlrIXztcjKHzifTvfgMA\nUC4oQQEAoD/l5ORQFDV9+nR6kclkvuqSXbkzMDBgMBgvX77ssef27dvHjRt3/fp14Zrx48dramqK\nzliTl5fX0tIyZcqUHkcbOXIkh8MpKCiQKlqKooKCggoLCzMzMzv91kcIYTKZ8+fPz83NFU7mlJ2d\nzWAwup1ath9HlnC79E4ePny4+EiGzifSv/sNAEC5oAQFAIC+6ujoePHiRVtb282bNwMDA01NTf38\n/OgmS0vL58+fZ2Zmtra2VlVVif7sQwjR1dV98uRJSUlJXV1da2trdna2LB/Koq6ubm5uXlpa2mNP\n+uJP0cljOBzOunXrMjIykpKSamtrCwsLV65caWRk5O/vL8loy5YtS05OjouLq62tbW9vLy0tffr0\nKSHEy8tr+PDh+fn5XV9169atvXv3Hjp0iMViMUTs27eP7hASElJRUbF169aGhoYrV65ERET4+flZ\nWVnRrQM3svhWGr2TbWxsxEcypD4RafcbAMDgQQEAKDD66XzyjkKJeXh4eHh4SPWS/fv30zeqqaur\nOzs7x8bG0nOijBkzpri4+ODBg3w+nxAyatSoP//8k6Iof39/FotlbGzMZDL5fP6CBQuKi4uFoz17\n9mz27NkcDsfMzOyzzz5bv349IcTS0vLRo0cUReXn548aNYrL5c6cObO8vPzMmTM8Hi88PFzatynh\nceLv729sbCy6JiAggMViCQQCejEjI4OejlVPT+/TTz/t9PL169e7uLgIFzs6OiIiIsaMGcNisXR0\ndFxdXe/cuUM39bjTmpubg4KCTE1NmUymvr6+u7t7UVERRVGurq6EkC1btnQN/lXTokZERAj7/PTT\n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\nsnHjxjlz5qxbt87Ozs7W1vbNN9/08vLqPJSRkdGaNWsuXbqUm5srtzQ0NBw4cEB7JuED79V5zMbG\nxpSUlMWLF69YsWL48OGenp4fffTRjRs3du7cqdvNx8fH2tp65MiRQUFB9fX1ly5d6u14/I+fn19N\nTU1sbOzDOuzZs+f3v/+9/EbcggULzMzMcnJyGhsbtR0YRgAAhiZjQycAAIODfL5CW1vb6dOn79y5\n8+KLL2ovyXVRlxH++Mc/xsfHq9VqeVYwMzPz5Zdftra27uRenQcsKyurq6ubMWOGtsXLy8vU1LS4\nuPiB/U1NTYUQ+pm+27NnT3JysvzP1tbWvr6+X375ZX5+vvYYxqEzjNnZ2d3sOagVFRUZOoXBiqED\nMNRQggLAQx08eHDbtm1lZWU1NTXakqOmpkYIYWNj09NolpaWf/rTn7Zt2/btt9/+5je/+fDDD3UP\n0njgvTp3584dOaxuo42NTW1tbU9z61s//fRTaWnp/fvNfvrpp9oSdOgMY2BgYJ/EGeDUarVarTZ0\nFgCAQYCFuADwYJcuXVq0aJGDg0NxcfHdu3e3bNkitz/xxBNCiBs3bvQiZnh4uImJSWpq6okTJ8aO\nHevm5tb5vTon128dKqU7d+44Ojr2Irc+9Pnnny9fvlyj49atW0ql8ujRo7/++qvcZ+gMo2YIEEJk\nZWUZOovBKisrq09+aQAwWFCCAsCDlZaWtrS0rF692tXVVaFQSJIktzs7O9vZ2R09erQXMR0dHZct\nW7Z///7Y2NiIiIgu79W5yZMnW1pafv/999qW4uLi5ubm6dOn9yK3vqLRaPbt2/fWW2/pNtra2gYE\nBLS1te3Zs0duYRgBABiaKEEB4MGcnJyEEMeOHWtqajp37pz2zUAzM7P169efOHEiPDz8ypUr7e3t\ntbW1Z86cEULY2dldvXq1oqKitrb2YatAo6KiWltbb9++/bvf/a7Le3UeU6FQREVF5ebmZmZm1tTU\nlJaWhoWFqVSq0NDQvh6MjgoKCh52KMs333xjbW397LPPdmgPCwsTOvviMowAAAxRhl5+AgAGsHTp\n0qVLl3bZLTo62s7OzsbGJiAgQD5D0s3N7dKlSxqNZvv27Z6engqFQqFQPP300zt27NBoNCUlJU8+\n+aRSqXzuuec2bNjg4OAghDA3N1+wYIFu2Dlz5nz88cfdvFfnMdvb27dt2/bUU0+ZmJjY2touWrTo\n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\n",
            "text/plain": [
              "<IPython.core.display.Image object>"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "w_-VsPdaOzne",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "from sklearn.model_selection import train_test_split\n",
        "doc_train, doc_test, que_train, que_test, ans_train, ans_test = train_test_split(train_doc_input, train_que_input, train_answer, test_size = 0.2, random_state = 0)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "PL_Gwjiq5Koe",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1465
        },
        "outputId": "a829fd37-9005-49b9-bd2d-44f463c947d2"
      },
      "source": [
        "import numpy as np\n",
        "model.compile(optimizer='sgd', loss='categorical_crossentropy')\n",
        "\n",
        "model.fit([np.array(doc_train), np.array(que_train)], np.array(ans_train),\n",
        "          validation_data=([np.array(doc_test), np.array(que_test)], np.array(ans_test)),\n",
        "          batch_size=128,\n",
        "          epochs=40)\n",
        "\n",
        "model.save('seq_model.h5')"
      ],
      "execution_count": 36,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "WARNING:tensorflow:From /usr/local/lib/python3.6/dist-packages/tensorflow/python/ops/math_ops.py:3066: to_int32 (from tensorflow.python.ops.math_ops) is deprecated and will be removed in a future version.\n",
            "Instructions for updating:\n",
            "Use tf.cast instead.\n",
            "Train on 1693 samples, validate on 424 samples\n",
            "Epoch 1/40\n",
            "1693/1693 [==============================] - 56s 33ms/step - loss: 1.4550 - val_loss: 1.4379\n",
            "Epoch 2/40\n",
            "1693/1693 [==============================] - 52s 30ms/step - loss: 1.4412 - val_loss: 1.4250\n",
            "Epoch 3/40\n",
            "1693/1693 [==============================] - 51s 30ms/step - loss: 1.4290 - val_loss: 1.4129\n",
            "Epoch 4/40\n",
            "1693/1693 [==============================] - 52s 30ms/step - loss: 1.4173 - val_loss: 1.4016\n",
            "Epoch 5/40\n",
            "1693/1693 [==============================] - 52s 31ms/step - loss: 1.4064 - val_loss: 1.3912\n",
            "Epoch 6/40\n",
            "1693/1693 [==============================] - 51s 30ms/step - loss: 1.3963 - val_loss: 1.3815\n",
            "Epoch 7/40\n",
            "1693/1693 [==============================] - 51s 30ms/step - loss: 1.3869 - val_loss: 1.3721\n",
            "Epoch 8/40\n",
            "1693/1693 [==============================] - 51s 30ms/step - loss: 1.3777 - val_loss: 1.3634\n",
            "Epoch 9/40\n",
            "1693/1693 [==============================] - 51s 30ms/step - loss: 1.3692 - val_loss: 1.3551\n",
            "Epoch 10/40\n",
            "1693/1693 [==============================] - 52s 31ms/step - loss: 1.3611 - val_loss: 1.3474\n",
            "Epoch 11/40\n",
            "1693/1693 [==============================] - 51s 30ms/step - loss: 1.3534 - val_loss: 1.3398\n",
            "Epoch 12/40\n",
            "1693/1693 [==============================] - 51s 30ms/step - loss: 1.3458 - val_loss: 1.3322\n",
            "Epoch 13/40\n",
            "1693/1693 [==============================] - 52s 30ms/step - loss: 1.3382 - val_loss: 1.3247\n",
            "Epoch 14/40\n",
            "1693/1693 [==============================] - 52s 30ms/step - loss: 1.3306 - val_loss: 1.3172\n",
            "Epoch 15/40\n",
            "1693/1693 [==============================] - 52s 31ms/step - loss: 1.3229 - val_loss: 1.3095\n",
            "Epoch 16/40\n",
            "1693/1693 [==============================] - 52s 31ms/step - loss: 1.3149 - val_loss: 1.3013\n",
            "Epoch 17/40\n",
            "1693/1693 [==============================] - 51s 30ms/step - loss: 1.3064 - val_loss: 1.2921\n",
            "Epoch 18/40\n",
            "1693/1693 [==============================] - 52s 31ms/step - loss: 1.2968 - val_loss: 1.2820\n",
            "Epoch 19/40\n",
            "1693/1693 [==============================] - 52s 30ms/step - loss: 1.2861 - val_loss: 1.2710\n",
            "Epoch 20/40\n",
            "1693/1693 [==============================] - 51s 30ms/step - loss: 1.2746 - val_loss: 1.2585\n",
            "Epoch 21/40\n",
            "1693/1693 [==============================] - 51s 30ms/step - loss: 1.2614 - val_loss: 1.2446\n",
            "Epoch 22/40\n",
            "1693/1693 [==============================] - 52s 31ms/step - loss: 1.2467 - val_loss: 1.2289\n",
            "Epoch 23/40\n",
            "1693/1693 [==============================] - 52s 30ms/step - loss: 1.2301 - val_loss: 1.2109\n",
            "Epoch 24/40\n",
            "1693/1693 [==============================] - 51s 30ms/step - loss: 1.2112 - val_loss: 1.1904\n",
            "Epoch 25/40\n",
            "1693/1693 [==============================] - 51s 30ms/step - loss: 1.1896 - val_loss: 1.1684\n",
            "Epoch 26/40\n",
            "1693/1693 [==============================] - 51s 30ms/step - loss: 1.1666 - val_loss: 1.1458\n",
            "Epoch 27/40\n",
            "1693/1693 [==============================] - 52s 30ms/step - loss: 1.1426 - val_loss: 1.1213\n",
            "Epoch 28/40\n",
            "1693/1693 [==============================] - 52s 31ms/step - loss: 1.1167 - val_loss: 1.0962\n",
            "Epoch 29/40\n",
            "1693/1693 [==============================] - 52s 30ms/step - loss: 1.0899 - val_loss: 1.0736\n",
            "Epoch 30/40\n",
            "1693/1693 [==============================] - 51s 30ms/step - loss: 1.0663 - val_loss: 1.0520\n",
            "Epoch 31/40\n",
            "1693/1693 [==============================] - 51s 30ms/step - loss: 1.0425 - val_loss: 1.0340\n",
            "Epoch 32/40\n",
            "1693/1693 [==============================] - 51s 30ms/step - loss: 1.0213 - val_loss: 1.0190\n",
            "Epoch 33/40\n",
            "1693/1693 [==============================] - 52s 30ms/step - loss: 1.0032 - val_loss: 1.0081\n",
            "Epoch 34/40\n",
            "1693/1693 [==============================] - 52s 31ms/step - loss: 0.9885 - val_loss: 0.9977\n",
            "Epoch 35/40\n",
            "1693/1693 [==============================] - 52s 30ms/step - loss: 0.9774 - val_loss: 0.9898\n",
            "Epoch 36/40\n",
            "1693/1693 [==============================] - 52s 30ms/step - loss: 0.9670 - val_loss: 0.9830\n",
            "Epoch 37/40\n",
            "1693/1693 [==============================] - 51s 30ms/step - loss: 0.9574 - val_loss: 0.9770\n",
            "Epoch 38/40\n",
            "1693/1693 [==============================] - 52s 30ms/step - loss: 0.9493 - val_loss: 0.9718\n",
            "Epoch 39/40\n",
            "1693/1693 [==============================] - 52s 31ms/step - loss: 0.9419 - val_loss: 0.9656\n",
            "Epoch 40/40\n",
            "1693/1693 [==============================] - 52s 31ms/step - loss: 0.9350 - val_loss: 0.9634\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "-8uqhzsjznTN",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "5423b7a5-9d8f-4146-ad9c-3e27036b506e"
      },
      "source": [
        "auth.authenticate_user()\n",
        "gauth = GoogleAuth()\n",
        "gauth.credentials = GoogleCredentials.get_application_default()\n",
        "drive = GoogleDrive(gauth)\n",
        "\n",
        "# upload model to drive\n",
        "upload1 = drive.CreateFile({'title': 'seq_model.h5'})\n",
        "upload1.SetContentFile('seq_model.h5')\n",
        "upload1.Upload()\n",
        "print (upload1['id'])"
      ],
      "execution_count": 41,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "1PM3N8_hgRzjCubwY0Opip6ASvglYX8Oa\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "xgGI_XQ-1KqD",
        "colab_type": "text"
      },
      "source": [
        "###2.3 Testing"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "aCJmWoezXBnO",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "ans_predict = model.predict([np.array(test_doc_input), np.array(test_que_input)])"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "_MUMfdsXu_Hk",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "#make predict answer lable list according to model predicted output\n",
        "predict_label = []\n",
        "for i in range(len(ans_predict)):\n",
        "  if len(ans_predict[i]) >= len(test_answer_list[i]):\n",
        "    for j in range(len(test_answer_list[i])):\n",
        "      if ans_predict[i][j] >= 0.5:\n",
        "        predict_label.append(1)\n",
        "      else:\n",
        "        predict_label.append(0)\n",
        "  else:\n",
        "    for j in range(len(ans_predict[i])):\n",
        "      if ans_predict[i][j] >= 0.5:\n",
        "        predict_label.append(1)\n",
        "      else:\n",
        "        predict_label.append(0)\n",
        "    diff = len(test_answer_list[i]) - len(ans_predict[i])\n",
        "    predict_label += [0] * diff"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "RRQn-uD60xcw",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "#make test answer label in a list\n",
        "answer_label = []\n",
        "for i in test_answer_list:\n",
        "  for j in i: \n",
        "      answer_label.append(j)\n"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "_C26VZ5c4hci",
        "colab_type": "code",
        "outputId": "cae342cc-fe7b-4819-b079-197bf0d15928",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 68
        }
      },
      "source": [
        "#calculate precision, recall and F-value\n",
        "from sklearn.metrics import precision_recall_fscore_support\n",
        "scores = precision_recall_fscore_support(np.array(predict_label), np.array(answer_label), average='weighted')\n",
        "print('Precision: ', scores[0], '\\nRecall: ', scores[1], '\\nF-score: ', scores[2])"
      ],
      "execution_count": 40,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Precision:  0.7751959753136629 \n",
            "Recall:  0.8116415958142577 \n",
            "F-score:  0.7622403820534213\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "z4jv_eVcyHIf",
        "colab_type": "text"
      },
      "source": [
        "##3. For Assesser"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "hLiEDST1wAU0",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "!pip install -U -q PyDrive\n",
        "from pydrive.auth import GoogleAuth\n",
        "from pydrive.drive import GoogleDrive\n",
        "from google.colab import auth\n",
        "from oauth2client.client import GoogleCredentials\n",
        "\n",
        "import pandas as pd\n",
        "\n",
        "\n",
        "# Authenticate and create the PyDrive client.\n",
        "auth.authenticate_user()\n",
        "gauth = GoogleAuth()\n",
        "gauth.credentials = GoogleCredentials.get_application_default()\n",
        "drive = GoogleDrive(gauth)\n",
        "\n",
        "# Download all three Microsoft BotBuilder Personality Chat Datasets on Google Colab virtual server\n",
        "\n",
        "id = '1TwuDSxlcAFDnTRpF-GRvqRXoR_UsJznH'\n",
        "downloaded = drive.CreateFile({'id':id }) \n",
        "downloaded.GetContentFile('WikiQA-test.tsv') \n",
        "\n",
        "df_test=pd.read_csv('WikiQA-test.tsv', sep='\\t')\n",
        "\n",
        "# download model from drive\n",
        "id = '1PM3N8_hgRzjCubwY0Opip6ASvglYX8Oa'\n",
        "downloaded = drive.CreateFile({'id':id}) \n",
        "downloaded.GetContentFile('seq_model.h5') \n",
        "\n",
        "import spacy\n",
        "nlp = spacy.load(\"en_core_web_sm\")\n",
        "\n",
        "def data_wrangling(df):\n",
        "  Q = {}\n",
        "  D = {}\n",
        "  Dpos = {}\n",
        "  Ddep = {}\n",
        "  Dent = {}\n",
        "  A = {}\n",
        "#   Apos = {}\n",
        "#   Adep = {}\n",
        "#   Aent = {}\n",
        "\n",
        "  for index, row in df.iterrows():\n",
        "    if row['QuestionID'] not in Q:\n",
        "      Q[row['QuestionID']] = []\n",
        "      token1 = nlp(row['Question'])\n",
        "      for i in token1:\n",
        "        Q[row['QuestionID']].append(i.text.lower())\n",
        "      Q[row['QuestionID']].append(row['DocumentID'])\n",
        "    if row['DocumentID'] not in D:\n",
        "      token2 = nlp(row['Sentence'])\n",
        "      D[row['DocumentID']] = []\n",
        "      Dpos[row['DocumentID']] = []\n",
        "      Ddep[row['DocumentID']] = []\n",
        "      Dent[row['DocumentID']] = []\n",
        "      temp = []\n",
        "      temppos = []\n",
        "      tempdep = []\n",
        "      tempent = []\n",
        "      for i in token2:\n",
        "        #get document token as well as its PoS tag, Dependency Path, and Named Entity tag\n",
        "        temp.append(i.text.lower())\n",
        "        temppos.append(i.pos_)\n",
        "        tempdep.append(i.dep_)\n",
        "        tempent.append(i.ent_type_)\n",
        "      D[row['DocumentID']].append(temp)\n",
        "      Dpos[row['DocumentID']].append(temppos)\n",
        "      Ddep[row['DocumentID']].append(tempdep)\n",
        "      Dent[row['DocumentID']].append(tempent)\n",
        "    else:\n",
        "      token2 = nlp(row['Sentence'])\n",
        "      temp = []\n",
        "      temppos = []\n",
        "      tempdep = []\n",
        "      tempent = []\n",
        "      for i in token2:\n",
        "        temp.append(i.text.lower())\n",
        "        temppos.append(i.pos_)\n",
        "        tempdep.append(i.dep_)\n",
        "        tempent.append(i.ent_type_)\n",
        "      D[row['DocumentID']].append(temp)\n",
        "      Dpos[row['DocumentID']].append(temppos)\n",
        "      Ddep[row['DocumentID']].append(tempdep)\n",
        "      Dent[row['DocumentID']].append(tempent)\n",
        "    if row['QuestionID'] not in A:\n",
        "      A[row['QuestionID']] = []\n",
        "      A[row['QuestionID']].append(row['Label'])\n",
        "    else:\n",
        "      A[row['QuestionID']].append(row['Label'])\n",
        "        \n",
        "  dataset = integrate_doc_data(Q, D, A)\n",
        "  pos = integrate_feature_data(Q, Dpos)\n",
        "  dep = integrate_feature_data(Q, Ddep)\n",
        "  ent = integrate_feature_data(Q, Dent)\n",
        "    \n",
        "  return dataset, pos, dep, ent\n",
        "\n",
        "    \n",
        "def integrate_doc_data(Q, D, A)  :\n",
        "  integrate_set = []\n",
        "  for key, value in Q.items():\n",
        "    data = {}\n",
        "    data[\"document\"] = D[value[-1]]\n",
        "    data[\"question\"] = value[: -1]\n",
        "    data[\"answer\"] = A[key]\n",
        "    \n",
        "    integrate_set.append(data)\n",
        "  return integrate_set\n",
        "\n",
        "def integrate_feature_data(Q, D)  :\n",
        "  integrate_set = []\n",
        "  for key, value in Q.items():\n",
        "    data = {}\n",
        "    data[\"document\"] = D[value[-1]]    \n",
        "    integrate_set.append(data)\n",
        "  return integrate_set\n",
        "  \n",
        "test_dataset, test_pos, test_dep, test_ent = data_wrangling(df_test)\n",
        "\n",
        "test_data_list = []\n",
        "for i in range(len(test_dataset)):\n",
        "  test_data_sublist = []\n",
        "  for j in range(len(test_dataset[i]['document'])):\n",
        "    temp = []\n",
        "    for l in range(len(test_dataset[i]['document'][j])):\n",
        "      temp.append([test_dataset[i]['document'][j][l], test_pos[i]['document'][j][l], test_dep[i]['document'][j][l], test_ent[i]['document'][j][l]])\n",
        "      if test_dataset[i]['document'][j][l] in test_dataset[i]['question']:\n",
        "        temp[l].append(1)\n",
        "      else:\n",
        "        temp[l].append(0)\n",
        "    test_data_sublist.append(temp)\n",
        "  test_data_list.append(test_data_sublist)\n",
        "\n",
        "test_question_list = []\n",
        "for i in test_dataset:\n",
        "  test_question_sublist = []\n",
        "  for j in i['question']:\n",
        "    test_question_sublist.append(j)\n",
        "  test_question_list.append(test_question_sublist)\n",
        "  \n",
        "test_answer_list = []\n",
        "for i in test_dataset:\n",
        "  test_answer_list.append(i['answer'])\n",
        "  \n",
        "#get unique token lists of documents and questions\n",
        "def doc_token_integration(dataset):\n",
        "  document_token = []\n",
        "  question_token = []\n",
        "  doc = []\n",
        "  for i in dataset:\n",
        "    for j in i['document']:\n",
        "      for l in j:\n",
        "        document_token.append(l)\n",
        "    for j in i['question']:\n",
        "      question_token.append(j)\n",
        "  return sorted(list(set(document_token))), sorted(list(set(question_token)))\n",
        "\n",
        "def feature_token_integration(dataset):\n",
        "  feature_token = []\n",
        "  \n",
        "  for i in dataset:\n",
        "    for j in i['document']:\n",
        "      for l in j:\n",
        "        feature_token.append(l)\n",
        "  return sorted(list(set(feature_token)))\n",
        "\n",
        "test_D_token, test_Q_token = doc_token_integration(test_dataset)\n",
        "test_Dpos_token = feature_token_integration(test_pos)\n",
        "test_Ddep_token = feature_token_integration(test_dep)\n",
        "test_Dent_token = feature_token_integration(test_ent)\n",
        "\n",
        "test_documents = []\n",
        "test_questions = []\n",
        "for i in test_dataset:  \n",
        "  test_questions.append(i['question'])\n",
        "  for j in i['document']:\n",
        "    test_documents.append(j)\n",
        "    \n",
        "#word2vec with skip-gram\n",
        "from gensim.models import Word2Vec\n",
        "wv_doc_test = Word2Vec(sentences=test_documents, size=100, window=5, min_count=5, workers=4, sg=1)\n",
        "wv_que_test = Word2Vec(sentences=test_questions, size=100, window=5, min_count=5, workers=4, sg=1)\n",
        "\n",
        "#generate feature dictionary to convert feature tokens to vectors\n",
        "def feature_embeddings(feature_list):\n",
        "  feature_index = {}\n",
        "  for i in feature_list:\n",
        "    index = [0] * len(feature_list)\n",
        "    index[feature_list.index(i)] = 1\n",
        "    feature_index[i] = index\n",
        "  return feature_index\n",
        "\n",
        "test_Dpos_index = feature_embeddings(test_Dpos_token)\n",
        "test_Ddep_index = feature_embeddings(test_Ddep_token)\n",
        "test_Dent_index = feature_embeddings(test_Dent_token)\n",
        "\n",
        "#generate document input\n",
        "def document_input(doc_list, model, Dpos_index = [], Ddep_index = [], Dent_index = [], Dmatch_index = False):\n",
        "  doc_input = []\n",
        "  for document in doc_list:\n",
        "    doc_subinput = []\n",
        "    #set the number of sentences in a document to be 20\n",
        "    if len(document) <= 20:\n",
        "      for sentence in document:\n",
        "        temp = []\n",
        "        #set the number of tokens in a sentence to be 40\n",
        "        if len(sentence) <= 40:\n",
        "          for i in sentence:\n",
        "            #add word vector\n",
        "            if i[0] in model.wv.vocab:\n",
        "              input_data = model.wv.word_vec(i[0]).tolist()\n",
        "            else:\n",
        "              #the size of word vector\n",
        "              input_data = [0] * 100\n",
        "            #add PoS tags\n",
        "            if Dpos_index != []:\n",
        "              pos_index = Dpos_index[i[1]]\n",
        "            else:\n",
        "              #the size of PoS tags\n",
        "              pos_index = [0] * 16\n",
        "            #add Dependency Path\n",
        "            if Ddep_index != []:\n",
        "              dep_index = Ddep_index[i[2]]\n",
        "            else:\n",
        "              #the size of Dependency Path\n",
        "              dep_index = [0] *46\n",
        "            #add Named Entity tags\n",
        "            if Dent_index != []:  \n",
        "              ent_index = Dent_index[i[3]]\n",
        "            else:\n",
        "              #the size of Named Entity tags\n",
        "              ent_index = [0] *19\n",
        "            for j in pos_index:\n",
        "              input_data.append(j)\n",
        "            for j in dep_index:\n",
        "              input_data.append(j)\n",
        "            for j in ent_index:\n",
        "              input_data.append(j)\n",
        "            #add Word match feature\n",
        "            if Dmatch_index is True:\n",
        "              input_data.append(i[4])\n",
        "            else:\n",
        "              input_data.append(0)\n",
        "            temp.append(input_data)\n",
        "          diff = 40 - len(sentence)\n",
        "          for i in range(diff):\n",
        "            temp.append([0]*len(temp[0]))\n",
        "        else:\n",
        "          sentence = sentence[:40]\n",
        "          for i in sentence:\n",
        "            if i[0] in model.wv.vocab:\n",
        "              input_data = model.wv.word_vec(i[0]).tolist()\n",
        "            else:\n",
        "              input_data = [0] * 100\n",
        "            if Dpos_index != []:\n",
        "              pos_index = Dpos_index[i[1]]\n",
        "            else:\n",
        "              pos_index = [0] * 16\n",
        "            if Ddep_index != []:\n",
        "              dep_index = Ddep_index[i[2]]\n",
        "            else:\n",
        "              dep_index = [0] *46\n",
        "            if Dent_index != []:  \n",
        "              ent_index = Dent_index[i[3]]\n",
        "            else:\n",
        "              ent_index = [0] *19\n",
        "            for j in pos_index:\n",
        "              input_data.append(j)\n",
        "            for j in dep_index:\n",
        "              input_data.append(j)\n",
        "            for j in ent_index:\n",
        "              input_data.append(j)\n",
        "            if Dmatch_index is True:\n",
        "              input_data.append(i[4])\n",
        "            else:\n",
        "              input_data.append(0)\n",
        "            temp.append(input_data)\n",
        "        doc_subinput.append(temp)\n",
        "      diff1 = 20 - len(document)\n",
        "      for l in range(diff1):\n",
        "        doc_subinput.append([[0]*len(temp[0])]*40)\n",
        "    else:\n",
        "      document = document[:20]\n",
        "      for sentence in document:\n",
        "        temp = []\n",
        "        if len(sentence) <= 40:\n",
        "          for i in sentence:\n",
        "            if i[0] in model.wv.vocab:\n",
        "              input_data = model.wv.word_vec(i[0]).tolist()\n",
        "            else:\n",
        "              input_data = [0] * 100\n",
        "            if Dpos_index != []:\n",
        "              pos_index = Dpos_index[i[1]]\n",
        "            else:\n",
        "              pos_index = [0] * 16\n",
        "            if Ddep_index != []:\n",
        "              dep_index = Ddep_index[i[2]]\n",
        "            else:\n",
        "              dep_index = [0] *46\n",
        "            if Dent_index != []:  \n",
        "              ent_index = Dent_index[i[3]]\n",
        "            else:\n",
        "              ent_index = [0] *19\n",
        "            for j in pos_index:\n",
        "              input_data.append(j)\n",
        "            for j in dep_index:\n",
        "              input_data.append(j)\n",
        "            for j in ent_index:\n",
        "              input_data.append(j)\n",
        "            if Dmatch_index is True:\n",
        "              input_data.append(i[4])\n",
        "            else:\n",
        "              input_data.append(0)\n",
        "            temp.append(input_data)\n",
        "          diff = 40 - len(sentence)\n",
        "          for i in range(diff):\n",
        "            temp.append([0]*len(temp[0]))\n",
        "        else:\n",
        "          sentence = sentence[:40]\n",
        "          for i in sentence:\n",
        "            if i[0] in model.wv.vocab:\n",
        "              input_data = model.wv.word_vec(i[0]).tolist()\n",
        "            else:\n",
        "              input_data = [0] * 100\n",
        "            if Dpos_index != []:\n",
        "              pos_index = Dpos_index[i[1]]\n",
        "            else:\n",
        "              pos_index = [0] * 16\n",
        "            if Ddep_index != []:\n",
        "              dep_index = Ddep_index[i[2]]\n",
        "            else:\n",
        "              dep_index = [0] *46\n",
        "            if Dent_index != []:  \n",
        "              ent_index = Dent_index[i[3]]\n",
        "            else:\n",
        "              ent_index = [0] *19\n",
        "            for j in pos_index:\n",
        "              input_data.append(j)\n",
        "            for j in dep_index:\n",
        "              input_data.append(j)\n",
        "            for j in ent_index:\n",
        "              input_data.append(j)\n",
        "            if Dmatch_index is True:\n",
        "              input_data.append(i[4])\n",
        "            else:\n",
        "              input_data.append(0)\n",
        "            temp.append(input_data)\n",
        "        doc_subinput.append(temp)\n",
        "      diff1 = 20 - len(document)\n",
        "      for l in range(diff1):\n",
        "        doc_subinput.append([[0]*len(temp[0])]*40)\n",
        "    doc_input.append(doc_subinput)\n",
        "  return doc_input\n",
        "\n",
        "test_doc_input = document_input(test_data_list, wv_doc_test, Dpos_index = test_Dpos_index, Ddep_index = test_Ddep_index, Dent_index = test_Dent_index, Dmatch_index = True)\n",
        "\n",
        "#generate question input\n",
        "def question_input(que_list, model):\n",
        "  que_input = []\n",
        "  for question in que_list:\n",
        "    que_subinput = []\n",
        "    #set the number of tokens in a question to be 20\n",
        "    if len(question) <= 20:\n",
        "      for i in question:\n",
        "        #add word vector\n",
        "        if i in model.wv.vocab:\n",
        "          input_data = model.wv.word_vec(i).tolist()\n",
        "        else:\n",
        "          #the size of word vector\n",
        "          input_data = [0] * 100\n",
        "        que_subinput.append(input_data)\n",
        "      diff = 20 - len(question)\n",
        "      for i in range(diff):\n",
        "        que_subinput.append([0] * 100)\n",
        "    else:\n",
        "      question = question[:20]\n",
        "      for i in question:\n",
        "        if i in model.wv.vocab:\n",
        "          input_data = model.wv.word_vec(i).tolist()\n",
        "        else:\n",
        "          input_data = [0] * 100\n",
        "        que_subinput.append(input_data)\n",
        "    que_input.append(que_subinput)\n",
        "  return que_input\n",
        "\n",
        "test_que_input = question_input(test_question_list, wv_que_test)\n",
        "\n",
        "#generate target answer output\n",
        "def answer_sentence_output(ans_list):\n",
        "  ans_output = []\n",
        "  for i in ans_list:\n",
        "    #the number of sentences in a document is 20\n",
        "    ans_suboutput = [0] * 20\n",
        "    if len(i) <= 20:\n",
        "      for j in range(len(i)):\n",
        "        ans_suboutput[j] = i[j]\n",
        "\n",
        "    else:\n",
        "      for j in range(20):\n",
        "        ans_suboutput[j] = i[j]\n",
        "    ans_output.append(ans_suboutput)\n",
        "  return ans_output\n",
        "\n",
        "test_answer = answer_sentence_output(test_answer_list)\n",
        "\n",
        "from tensorflow import keras\n",
        "new_model = keras.models.load_model('seq_model.h5')\n",
        "\n",
        "import numpy as np\n",
        "new_ans_predict = new_model.predict([np.array(test_doc_input), np.array(test_que_input)])\n",
        "predict_label = []\n",
        "for i in range(len(new_ans_predict)):\n",
        "  if len(new_ans_predict[i]) >= len(test_answer_list[i]):\n",
        "    for j in range(len(test_answer_list[i])):\n",
        "      if new_ans_predict[i][j] >= 0.5:\n",
        "        predict_label.append(1)\n",
        "      else:\n",
        "        predict_label.append(0)\n",
        "  else:\n",
        "    for j in range(len(new_ans_predict[i])):\n",
        "      if new_ans_predict[i][j] >= 0.5:\n",
        "        predict_label.append(1)\n",
        "      else:\n",
        "        predict_label.append(0)\n",
        "    diff = len(test_answer_list[i]) - len(new_ans_predict[i])\n",
        "    predict_label += [0] * diff\n",
        "    \n",
        "#make test answer label in a list    \n",
        "answer_label = []\n",
        "for i in test_answer_list:\n",
        "  for j in i: \n",
        "      answer_label.append(j)\n",
        "\n",
        "#calculate precision, recall and F-value\n",
        "from sklearn.metrics import precision_recall_fscore_support\n",
        "scores = precision_recall_fscore_support(np.array(predict_label), np.array(answer_label), average='macro')\n",
        "print('Precision: ', scores[0], '\\nRecall: ', scores[1], '\\nF-score: ', scores[2])\n"
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}