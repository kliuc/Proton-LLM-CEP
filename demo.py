import streamlit as st
import pandas as pd
from proton_driver import client
from gemini_udf import check_palindrome

c = client.Client(host='127.0.0.1', port=8463)

query = '''SELECT
    character,
    array_concat(array_cast(character), lags(character, 1, 2, '')) AS sequence
FROM
    rand_abc'''

rows = c.execute_iter(query)
st.code(query, language='sql')

df = pd.DataFrame(columns=['character', 'sequence', 'is_palindrome'])
cache = {}

with st.empty():
    for row in rows:
        data = list(row)
        sequence = ''.join(data[1])
        if sequence not in cache:
            cache[sequence] = check_palindrome(sequence)
        data.append(cache[sequence])
        df = pd.concat([df, pd.DataFrame([data], columns=df.columns)], ignore_index=True).tail(10)
        st.table(df)