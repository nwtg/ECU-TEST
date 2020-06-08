<?xml version="1.0" encoding="utf-8"?>
<ATTRIBUTES format-rev="1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	<ATTRIBUTE-DEFINITIONS>
		<DEFINITION format-rev="1" xsi:type="anAttributeDef">
			<NAME xsi:type="string">Estimated Duration [min]</NAME>
			<REQUIRED xsi:type="boolean">False</REQUIRED>
		</DEFINITION>
		<DEFINITION format-rev="2" xsi:type="anAttributeTreeValueDef">
			<NAME xsi:type="string">Execution Priority</NAME>
			<REQUIRED xsi:type="boolean">False</REQUIRED>
			<NODE-META-LIST-NON-LEAFS>
				<ELEMENT format-rev="1" xsi:type="anAttributeTreeNodeMetaEntryDef">
					<USE-AS-IDENTIFIER xsi:type="boolean">True</USE-AS-IDENTIFIER>
				</ELEMENT>
			</NODE-META-LIST-NON-LEAFS>
			<NODE-META-LIST-LEAFS>
				<ELEMENT format-rev="1" xsi:type="anAttributeTreeNodeMetaEntryDef">
					<USE-AS-IDENTIFIER xsi:type="boolean">True</USE-AS-IDENTIFIER>
				</ELEMENT>
			</NODE-META-LIST-LEAFS>
			<NODE-LIST>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">1</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">2</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">3</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">4</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">5</VALUE>
					</VALUE-LIST>
				</ELEMENT>
			</NODE-LIST>
		</DEFINITION>
		<DEFINITION format-rev="2" xsi:type="anAttributeTreeValueDef">
			<NAME xsi:type="string">Testlevel</NAME>
			<REQUIRED xsi:type="boolean">False</REQUIRED>
			<IS-MULTI-CHOICE xsi:type="boolean">True</IS-MULTI-CHOICE>
			<NODE-META-LIST-NON-LEAFS>
				<ELEMENT format-rev="1" xsi:type="anAttributeTreeNodeMetaEntryDef">
					<USE-AS-IDENTIFIER xsi:type="boolean">True</USE-AS-IDENTIFIER>
				</ELEMENT>
			</NODE-META-LIST-NON-LEAFS>
			<NODE-META-LIST-LEAFS>
				<ELEMENT format-rev="1" xsi:type="anAttributeTreeNodeMetaEntryDef">
					<USE-AS-IDENTIFIER xsi:type="boolean">True</USE-AS-IDENTIFIER>
				</ELEMENT>
			</NODE-META-LIST-LEAFS>
			<NODE-LIST>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">component</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">module</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">not specified</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">subsystem</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">system</VALUE>
					</VALUE-LIST>
				</ELEMENT>
			</NODE-LIST>
		</DEFINITION>
		<DEFINITION format-rev="1" xsi:type="anAttributeDef">
			<NAME xsi:type="string">Designer</NAME>
			<REQUIRED xsi:type="boolean">False</REQUIRED>
		</DEFINITION>
		<DEFINITION format-rev="1" xsi:type="anAttributeDef">
			<NAME xsi:type="string">Design Contact</NAME>
			<REQUIRED xsi:type="boolean">False</REQUIRED>
		</DEFINITION>
		<DEFINITION format-rev="1" xsi:type="anAttributeDef">
			<NAME xsi:type="string">Design Department</NAME>
			<REQUIRED xsi:type="boolean">False</REQUIRED>
		</DEFINITION>
		<DEFINITION format-rev="1" xsi:type="anAttributeDef">
			<NAME xsi:type="string">Test Comment</NAME>
			<REQUIRED xsi:type="boolean">False</REQUIRED>
		</DEFINITION>
		<DEFINITION format-rev="1" xsi:type="anAttributeDef">
			<NAME xsi:type="string">Tools</NAME>
			<REQUIRED xsi:type="boolean">False</REQUIRED>
		</DEFINITION>
		<DEFINITION format-rev="1" xsi:type="anAttributeDef">
			<NAME xsi:type="string">VersionCounter</NAME>
			<REQUIRED xsi:type="boolean">False</REQUIRED>
		</DEFINITION>
		<DEFINITION format-rev="2" xsi:type="anAttributeTreeValueDef">
			<NAME xsi:type="string">Plan Scope</NAME>
			<REQUIRED xsi:type="boolean">False</REQUIRED>
			<DEFAULT-VALUE xsi:type="string"/>
			<ORIGIN xsi:type="string">TMS</ORIGIN>
			<IS-MULTI-CHOICE xsi:type="boolean">True</IS-MULTI-CHOICE>
			<NODE-META-LIST-NON-LEAFS>
				<ELEMENT format-rev="1" xsi:type="anAttributeTreeNodeMetaEntryDef">
					<USE-AS-IDENTIFIER xsi:type="boolean">True</USE-AS-IDENTIFIER>
				</ELEMENT>
			</NODE-META-LIST-NON-LEAFS>
			<NODE-META-LIST-LEAFS>
				<ELEMENT format-rev="1" xsi:type="anAttributeTreeNodeMetaEntryDef">
					<USE-AS-IDENTIFIER xsi:type="boolean">True</USE-AS-IDENTIFIER>
				</ELEMENT>
			</NODE-META-LIST-LEAFS>
			<NODE-LIST>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Iteration 32 (2017-07-31)</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Iteration 33 (2017-08-31)</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Iteration 34 (2017-09-30)</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Iteration 35 (2017-10-31)</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Version 1.0 (2017-07-31)</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Version 2.0 (2017-10-31)</VALUE>
					</VALUE-LIST>
				</ELEMENT>
			</NODE-LIST>
		</DEFINITION>
		<DEFINITION format-rev="2" xsi:type="anAttributeTreeValueDef">
			<NAME xsi:type="string">Platform</NAME>
			<REQUIRED xsi:type="boolean">False</REQUIRED>
			<DEFAULT-VALUE xsi:type="string"/>
			<ORIGIN xsi:type="string">TMS</ORIGIN>
			<NODE-META-LIST-NON-LEAFS>
				<ELEMENT format-rev="1" xsi:type="anAttributeTreeNodeMetaEntryDef">
					<USE-AS-IDENTIFIER xsi:type="boolean">True</USE-AS-IDENTIFIER>
				</ELEMENT>
			</NODE-META-LIST-NON-LEAFS>
			<NODE-META-LIST-LEAFS>
				<ELEMENT format-rev="1" xsi:type="anAttributeTreeNodeMetaEntryDef">
					<USE-AS-IDENTIFIER xsi:type="boolean">True</USE-AS-IDENTIFIER>
				</ELEMENT>
			</NODE-META-LIST-LEAFS>
			<NODE-LIST>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Linux</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Mac OS X</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">MS Windows</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Other</VALUE>
					</VALUE-LIST>
				</ELEMENT>
			</NODE-LIST>
		</DEFINITION>
		<DEFINITION format-rev="2" xsi:type="anAttributeTreeValueDef">
			<NAME xsi:type="string">Status</NAME>
			<REQUIRED xsi:type="boolean">True</REQUIRED>
			<DEFAULT-VALUE xsi:type="string"/>
			<ORIGIN xsi:type="string">TMS</ORIGIN>
			<NODE-META-LIST-NON-LEAFS>
				<ELEMENT format-rev="1" xsi:type="anAttributeTreeNodeMetaEntryDef">
					<USE-AS-IDENTIFIER xsi:type="boolean">True</USE-AS-IDENTIFIER>
				</ELEMENT>
			</NODE-META-LIST-NON-LEAFS>
			<NODE-META-LIST-LEAFS>
				<ELEMENT format-rev="1" xsi:type="anAttributeTreeNodeMetaEntryDef">
					<USE-AS-IDENTIFIER xsi:type="boolean">True</USE-AS-IDENTIFIER>
				</ELEMENT>
			</NODE-META-LIST-LEAFS>
			<NODE-LIST>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Failed</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">In Progress</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Open</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Passed</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Rejected</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Reopened</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Verified Failed</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Verified Passed</VALUE>
					</VALUE-LIST>
				</ELEMENT>
			</NODE-LIST>
		</DEFINITION>
		<DEFINITION format-rev="2" xsi:type="anAttributeTreeValueDef">
			<NAME xsi:type="string">Project Span</NAME>
			<REQUIRED xsi:type="boolean">False</REQUIRED>
			<DEFAULT-VALUE xsi:type="string"/>
			<ORIGIN xsi:type="string">TMS</ORIGIN>
			<READONLY xsi:type="boolean">True</READONLY>
			<IS-MULTI-CHOICE xsi:type="boolean">True</IS-MULTI-CHOICE>
			<NODE-META-LIST-NON-LEAFS>
				<ELEMENT format-rev="1" xsi:type="anAttributeTreeNodeMetaEntryDef">
					<USE-AS-IDENTIFIER xsi:type="boolean">True</USE-AS-IDENTIFIER>
				</ELEMENT>
			</NODE-META-LIST-NON-LEAFS>
			<NODE-META-LIST-LEAFS>
				<ELEMENT format-rev="1" xsi:type="anAttributeTreeNodeMetaEntryDef">
					<USE-AS-IDENTIFIER xsi:type="boolean">True</USE-AS-IDENTIFIER>
				</ELEMENT>
			</NODE-META-LIST-LEAFS>
			<NODE-LIST>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Document Library</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Drive Pilot</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">E-Library</VALUE>
					</VALUE-LIST>
				</ELEMENT>
			</NODE-LIST>
		</DEFINITION>
		<DEFINITION format-rev="2" xsi:type="anAttributeTreeValueDef">
			<NAME xsi:type="string">Keep In History</NAME>
			<REQUIRED xsi:type="boolean">False</REQUIRED>
			<DEFAULT-VALUE xsi:type="string"/>
			<ORIGIN xsi:type="string">TMS</ORIGIN>
			<NODE-META-LIST-NON-LEAFS>
				<ELEMENT format-rev="1" xsi:type="anAttributeTreeNodeMetaEntryDef">
					<USE-AS-IDENTIFIER xsi:type="boolean">True</USE-AS-IDENTIFIER>
				</ELEMENT>
			</NODE-META-LIST-NON-LEAFS>
			<NODE-META-LIST-LEAFS>
				<ELEMENT format-rev="1" xsi:type="anAttributeTreeNodeMetaEntryDef">
					<USE-AS-IDENTIFIER xsi:type="boolean">True</USE-AS-IDENTIFIER>
				</ELEMENT>
			</NODE-META-LIST-LEAFS>
			<NODE-LIST>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">false</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">true</VALUE>
					</VALUE-LIST>
				</ELEMENT>
			</NODE-LIST>
		</DEFINITION>
		<DEFINITION format-rev="2" xsi:type="anAttributeTreeValueDef">
			<NAME xsi:type="string">Type</NAME>
			<REQUIRED xsi:type="boolean">False</REQUIRED>
			<DEFAULT-VALUE xsi:type="string"/>
			<ORIGIN xsi:type="string">TMS</ORIGIN>
			<READONLY xsi:type="boolean">True</READONLY>
			<NODE-META-LIST-NON-LEAFS>
				<ELEMENT format-rev="1" xsi:type="anAttributeTreeNodeMetaEntryDef">
					<USE-AS-IDENTIFIER xsi:type="boolean">True</USE-AS-IDENTIFIER>
				</ELEMENT>
			</NODE-META-LIST-NON-LEAFS>
			<NODE-META-LIST-LEAFS>
				<ELEMENT format-rev="1" xsi:type="anAttributeTreeNodeMetaEntryDef">
					<USE-AS-IDENTIFIER xsi:type="boolean">True</USE-AS-IDENTIFIER>
				</ELEMENT>
			</NODE-META-LIST-LEAFS>
			<NODE-LIST>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Automated</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Manual</VALUE>
					</VALUE-LIST>
				</ELEMENT>
			</NODE-LIST>
		</DEFINITION>
		<DEFINITION format-rev="1" xsi:type="anAttributeDef">
			<NAME xsi:type="string">Template</NAME>
			<REQUIRED xsi:type="boolean">False</REQUIRED>
			<DEFAULT-VALUE xsi:type="string"/>
			<ORIGIN xsi:type="string">TMS</ORIGIN>
			<READONLY xsi:type="boolean">True</READONLY>
		</DEFINITION>
		<DEFINITION format-rev="1" xsi:type="anAttributeDef">
			<NAME xsi:type="string">Use Report From Template</NAME>
			<REQUIRED xsi:type="boolean">False</REQUIRED>
			<DEFAULT-VALUE xsi:type="string"/>
			<ORIGIN xsi:type="string">TMS</ORIGIN>
			<READONLY xsi:type="boolean">True</READONLY>
		</DEFINITION>
		<DEFINITION format-rev="1" xsi:type="anAttributeDef">
			<NAME xsi:type="string">Group ID</NAME>
			<REQUIRED xsi:type="boolean">False</REQUIRED>
			<DEFAULT-VALUE xsi:type="string"/>
			<ORIGIN xsi:type="string">TMS</ORIGIN>
		</DEFINITION>
		<DEFINITION format-rev="1" xsi:type="anAttributeDef">
			<NAME xsi:type="string">Summary Defect</NAME>
			<REQUIRED xsi:type="boolean">False</REQUIRED>
			<DEFAULT-VALUE xsi:type="string"/>
			<ORIGIN xsi:type="string">TMS</ORIGIN>
			<READONLY xsi:type="boolean">True</READONLY>
		</DEFINITION>
		<DEFINITION format-rev="1" xsi:type="anAttributeDef">
			<NAME xsi:type="string">Finished On</NAME>
			<REQUIRED xsi:type="boolean">False</REQUIRED>
			<DEFAULT-VALUE xsi:type="string"/>
			<ORIGIN xsi:type="string">TMS</ORIGIN>
		</DEFINITION>
	</ATTRIBUTE-DEFINITIONS>
</ATTRIBUTES>
