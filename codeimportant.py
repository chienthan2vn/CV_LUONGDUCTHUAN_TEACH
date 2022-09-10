#Ngăn chặn tắc nghẽn bộ nhớ với phần train_dataset
AUTOTUNE = tf.data.experimental.AUTOTUNE
train_dataset = train_dataset.prefetch(buffer_size=AUTOTUNE)
#Train tiếp sau khi điều chỉnh cấu trúc với initial_epoch=history.epoch[-1], total là tổng epochs và inital là epochs lúc đầu
history_fine = model2.fit(train_dataset, epochs=total_epochs, initial_epoch=history.epoch[-1], validation_data=validation_dataset)
