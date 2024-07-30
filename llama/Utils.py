

class utils:

    @staticmethod
    def convert_safetensor_2_pth(para_dict):
        list_sts = ['model.', 'embed_tokens', 'self_attn', 'k_proj', 'o_proj', 'q_proj', 'v_proj', 'mlp',
                    'down_proj', 'gate_proj', 'up_proj', 'input_layernorm', 'post_attention_layernorm', 'lm_head']
        list_pth = ['', 'tok_embeddings', 'attention', 'wk', 'wo', 'wq', 'wv', 'feed_forward', 'w2', 'w1', 'w3',
                    'attention_norm', 'ffn_norm', 'output']
        for key in list(para_dict.keys()):
            new_key = key
            for index, item in enumerate(list_sts):
                if item in key:
                    new_key = new_key.replace(item, list_pth[index])
            print(new_key)

            para_dict[new_key] = para_dict.pop(key)

        print(para_dict.keys())
