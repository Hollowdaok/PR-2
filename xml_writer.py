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
        scores = content["actual_record"]["scores"]
        
        for course, score in zip(courses, scores):
            course_node = ET.SubElement(actual_node, "course")
            course_node.set("title", course)
            course_node.text = str(score)
        
        mean_node = ET.SubElement(actual_node, "mean")
        mean_node.text = str(content["actual_record"]["mean"])
        
        target_node = ET.SubElement(root, "target_record")
        target_courses = content["target_record"]["target_courses"]
        target_scores = content["target_record"]["target_scores"]
        
        for course, score in zip(target_courses, target_scores):
            course_node = ET.SubElement(target_node, "target_course")
            course_node.set("title", course)
            course_node.text = str(score)
        
        target_mean_node = ET.SubElement(target_node, "target_mean")
        target_mean_node.text = str(content["target_record"]["target_mean"])
        
        xml_tree = ET.ElementTree(root)
        ET.indent(xml_tree, space="  ")
        xml_tree.write(path, encoding="utf-8", xml_declaration=True)