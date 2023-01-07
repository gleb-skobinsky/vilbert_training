import json
import codecs


def read_file(filename: str):
    with codecs.open(filename, "r", encoding="utf-8") as file:
        text = file.read()
        file.close()
    return json.loads(text)


def write_file(filename: str, input: dict):
    string_to_write = (
        json.dumps(input, ensure_ascii=False).encode("utf8").decode("utf-8")
    )
    print(string_to_write)
    with open(filename, "w") as file:
        file.write(string_to_write)
        file.close()


if __name__ == "__main__":
    russian_dict = read_file("vqa_answers_rus.json")
    rus_questions_dict = read_file("vqa_questions_rus.json")
    transformed_dict = {"annotations": []}

    for key, value in russian_dict.items():
        transformed_dict["annotations"].append(
            {
                "question_type": "",
                "multiple_choice_answer": value["answer"][0],
                "answers": list(
                    [
                        {
                            "answer": item,
                            "answer_confidence": "yes",
                            "answer_id": index + 1,
                        }
                        for index, item in enumerate(value["answer"])
                    ]
                ),
                "image_id": rus_questions_dict[key]["image_id"],
                "answer_type": "other",
                "question_id": int(key),
            }
        )
    write_file("rus_mscoco_train2014_annotations.json", transformed_dict)
