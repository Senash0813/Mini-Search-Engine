import streamlit as st

def run_ui(agent_executor, parser):
    # Add custom CSS for a hue-changing background
    st.markdown(
        """
        <style>
            body {
                animation: hue-rotate 10s infinite;
                background: linear-gradient(120deg, #001f3f, #0074D9); /* Dark blue and light blue */
                background-size: 400% 400%;
            }
            @keyframes hue-rotate {
                0% {
                    filter: hue-rotate(0deg);
                }
                50% {
                    filter: hue-rotate(180deg);
                }
                100% {
                    filter: hue-rotate(360deg);
                }
            }
            .centered-title {
                text-align: center;
                color: black;
                font-size: 2.5em;
                font-weight: bold;
            }
            .description {
                text-align: center;
                color: grey;
                font-size: 1.2em;
                margin-bottom: 20px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Title and description
    st.markdown("<div class='centered-title'>Mini Search Engine</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='description'>This Mini Search Engine helps you find answers for your questions using an LLM(answers can be incorrect so check sources).</div>",
        unsafe_allow_html=True,
    )

    # Center the input box and question
    st.markdown(
        "<div style='text-align: center;'><h3>What can I help you with?</h3></div>",
        unsafe_allow_html=True,
    )
    query = st.text_area("Enter your query below:", "", height=150, label_visibility="collapsed")

    # Submit button
    if st.button("Submit"):
        if query.strip():
            with st.spinner("Processing..."):
                try:
                    # Invoke the agent and parse the response
                    raw_response = agent_executor.invoke({"query": query})
                    structured_response = parser.parse(raw_response.get("output"))

                    # Display the output in a nicer way
                    st.markdown("## Results")
                    st.markdown("### Summary")
                    st.markdown(
                        f"<div style='background-color: #f9f9f9; padding: 10px; border-radius: 5px;'>{structured_response.summary}</div>",
                        unsafe_allow_html=True,
                    )

                    st.markdown("### Tools Used")
                    st.markdown(
                        f"<div style='background-color: #f0f0f0; padding: 10px; border-radius: 5px;'>{', '.join(structured_response.tools_used)}</div>",
                        unsafe_allow_html=True,
                    )

                    st.markdown("### Sources")
                    for source in structured_response.sources:
                        st.markdown(
                            f"<div style='background-color: #f7f7f7; padding: 10px; border-radius: 5px;'><a href='{source}' target='_blank'>{source}</a></div>",
                            unsafe_allow_html=True,
                        )
                except Exception as e:
                    st.error(f"Error parsing response: {e}")
        else:
            st.warning("Please enter a query.")