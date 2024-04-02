import json,copy


DEFAULT_IMAGE_TOKEN = "<image>"
data_path = "./llava_test.json"
list_data_dict = json.load(open(data_path, "r"))

sources = list_data_dict[1]
print(sources)
sources = [sources]
# assert len(sources) == 1, "Don't know why it is wrapped to a list"  # FIXME

print("$$$$$$$")
print(sources[0])
print('image' in sources[0])

x=[e["conversations"] for e in sources]
print("&&&&&&&")

print(x)

for source in x:
    for sentence in source:
        if DEFAULT_IMAGE_TOKEN in sentence['value']:
            print("*****")
            print(sentence['value'])
            sentence['value'] = sentence['value'].replace(DEFAULT_IMAGE_TOKEN, '').strip()
            print("*****")
            print(sentence['value'])
            print("****")
            sentence['value'] = DEFAULT_IMAGE_TOKEN + '\n' + sentence['value']
            sentence['value'] = sentence['value'].strip()
            print(sentence['value'])
            print("……………………")
        #     if "mmtag" in conversation_lib.default_conversation.version:
        #         sentence['value'] = sentence['value'].replace(DEFAULT_IMAGE_TOKEN, '<Image>' + DEFAULT_IMAGE_TOKEN + '</Image>')
        # replace_token = DEFAULT_IMAGE_TOKEN
        # if data_args.mm_use_im_start_end:
        #     replace_token = DEFAULT_IM_START_TOKEN + replace_token + DEFAULT_IM_END_TOKEN
        # sentence["value"] = sentence["value"].replace(DEFAULT_IMAGE_TOKEN, replace_token)

    # return sources
