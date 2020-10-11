from kafka import KafkaConsumer

class ConsumerServer(KafkaConsumer):
    def __init__(self, topic_name):
        self.consumer = KafkaConsumer(bootstrap_servers = "localhost:9092", )   
        self.consumer.subscribe(topics = topic_name)
    
    def consume(self):
        try:
            while True:
                for metadata,consumer_record in self.consumer.poll().items():
                    print(f"metadata: {metadata} consumer_record: {consumer_record}")
                    if consumer_record:
                        for record in consumer_record:
                            print(record.value)
                    else:
                        print("No message received by consumer")
                time.sleep(0.5)
        except:
            print("Closing consumer")
            self.consumer.close()
            
if __name__ == "__main__":
    consumer = ConsumerServer("police.service.calls")
    consumer.consume()
