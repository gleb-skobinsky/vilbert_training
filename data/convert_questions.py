from convert_answers import read_file, write_file

if __name__ == "__main__":
    russian_dict = read_file("vqa_questions_rus.json")
    transformed_dict = {"questions": []}
    for key, value in russian_dict.items():
        transformed_dict["questions"].append(
            {
                "image_id": value["image_id"],
                "question": value["question"],
                "question_id": int(key),
            }
        )
    write_file("rus_OpenEnded_mscoco_train2014_questions.json", transformed_dict)
