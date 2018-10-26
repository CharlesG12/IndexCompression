import ProcessDoc

doc_path = 'D:\\Classes\\CSS6322 Information Retrival\\HW1\Token\\data\\'

stem_processor = ProcessDoc.ProcessDoc(doc_path, 0, 1)
stem_processor.run()
stem_dic = stem_processor.collection_dic

lemma_processor = ProcessDoc.ProcessDoc(doc_path, 1, 0)
lemma_processor.run()
lemma_dic = lemma_processor.collection_dic


