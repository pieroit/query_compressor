

from cat.log import log
from cat.mad_hatter.decorators import hook

@hook
def cat_recall_query(user_message, cat):
    

    conversation_so_far  = cat.stringify_chat_history(latest_n=5)

    prompt = f"""Here is a conversation between an AI and a Human:
{conversation_so_far}

Sum up in a single sentence what the human wants in their own language, keeping all the details from the conversation.
The sentence must be expressed from the point of view of the human. Beware of topic changes.

Sentence: """

    compressed_query = cat.llm(prompt)

    return compressed_query