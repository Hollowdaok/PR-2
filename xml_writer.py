import xml.etree.ElementTree as ET
from file_writer import FileWriter

class XmlWriter(FileWriter):
    def write_to_file(self, content: dict, path: str):
        root = ET.Element("student")
        
        name_node = ET.SubElement(root, "name")
        name_node.text = content["name"]
        
        group_node = ET.SubElement(root, "group")
        group_node.text = content["group"]
        
        actual_node = ET.SubElement(root, "actual_record")
        courses = content["actual_record"]["courses"]
        scores_dict = content["actual_record"]["scores"]
        means = content["actual_record"]["mean_per_course"]
        
        for course in courses:
            course_node = ET.SubElement(actual_node, "course")
            course_node.set("title", course)
            
            scores_node = ET.SubElement(course_node, "scores")
            for score in scores_dict[course]:
                score_node = ET.SubElement(scores_node, "score")
                score_node.text = str(score)
            
            mean_node = ET.SubElement(course_node, "mean")
            mean_node.text = str(means[course])
        
        target_node = ET.SubElement(root, "target_record")
        target_scores_dict = content["target_record"]["target_scores"]
        target_means = content["target_record"]["mean_per_course"]
        
        for course in courses:
            course_node = ET.SubElement(target_node, "target_course")
            course_node.set("title", course)
            
            scores_node = ET.SubElement(course_node, "target_scores")
            for score in target_scores_dict[course]:
                score_node = ET.SubElement(scores_node, "score")
                score_node.text = str(score)
            
            mean_node = ET.SubElement(course_node, "mean")
            mean_node.text = str(target_means[course])
        
        xml_tree = ET.ElementTree(root)
        ET.indent(xml_tree, space="  ")
        xml_tree.write(path, encoding="utf-8", xml_declaration=True)