from gradio_client import Client

# client = Client("https://sanchit-gandhi-whisper-jax.hf.space/")
# result = client.predict(
# 				"1.wav",	# str (filepath or URL to file) in 'inputs' Audio component
# 				"transcribe",	# str in 'Task' Radio component
# 				True,	# bool in 'Return timestamps' Checkbox component
# 				api_name="/predict"
# )
# print(result)
text = "('[00:00.000 -> 00:26.000]  У-у-у, у девчонки! Ах, вы девчонки! Ах, вы девчонки!\n[00:26.000 -> 00:28.000]  Ах, вы девчонки!\n[00:28.000 -> 00:30.000]  Ах, вы девчонки!\n[00:30.000 -> 00:32.000]  Ах, вы девчонки!\n[00:32.000 -> 00:34.000]  Ах, вы девчонки!\n[00:34.000 -> 00:36.000]  Привет, девочки!\n[00:36.000 -> 00:38.000]  Ой, Женька, ты русалка!\n[00:38.000 -> 00:40.000]  Ой, Женька, ты русалка!\n[00:40.000 -> 00:42.000]  У тебя кожа прозрачная.\n[00:42.000 -> 00:44.000]  Хоть скульптуру выпей.\n[00:44.000 -> 00:46.000]  Красивая.\n[00:46.000 -> 00:48.000]  Такую фигуру в обмундирование поковать.\n[00:50.000 -> 00:52.000]  А ну-ка я вам всех спартов отбавлю!', '4.897148370742798')"
print(text)


# from whisper_jax import FlaxWhisperPipline
# import whisper
#
# model = whisper.load_model("large")
# result = model.transcribe("1.wav")
# print(result["text"])



# instantiate pipeline
# pipeline = FlaxWhisperPipline("openai/whisper-large-v2")
#
# # JIT compile the forward call - slow, but we only do once
# text = pipeline("1.wav")
# print(text)

# used cached function thereafter - super fast!!
# text = pipeline("audio.mp3")






