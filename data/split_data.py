from convert_answers import read_file, write_file
import random
from copy import deepcopy

questions_data = read_file("rus_OpenEnded_mscoco_val2014_questions.json")
answers_data = read_file("rus_mscoco_val2014_annotations.json")
questions_val_data = deepcopy(questions_data)
answers_val_data = deepcopy(answers_data)

questions_list = questions_data["questions"]
answers_list = answers_data["annotations"]
split_margin = round(len(questions_list) * 0.9)
random.shuffle(questions_list)
(train_questions, val_questions) = (
    questions_list[:split_margin],
    questions_list[split_margin:],
)

questions_data["questions"] = train_questions
questions_val_data["questions"] = val_questions

train_q_ids = set([i["question_id"] for i in train_questions])
val_q_ids = set([i["question_id"] for i in val_questions])

train_answers = list(filter(lambda x: x["question_id"] in train_q_ids, answers_list))
val_answers = list(filter(lambda x: x["question_id"] in val_q_ids, answers_list))

answers_data["annotations"] = train_answers
answers_val_data["annotations"] = val_answers

write_file("rus_OpenEnded_mscoco_train2014_questions.json", questions_data)
write_file("rus_OpenEnded_mscoco_val2014_questions.json", questions_val_data)
write_file("rus_mscoco_train2014_annotations.json", answers_data)
write_file("rus_mscoco_val2014_annotations.json", answers_val_data)
